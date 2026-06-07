---
title: "Blackwell Server Setup for vLLM"
date: 2026-05-28
author: Becze Szabolcs
status: active
description: "Complete setup instructions for deploying vLLM with MiniMax M2.1 model on NVIDIA Blackwell GPUs running Ubuntu 22.04, including driver installation, Docker configuration, and OpenAI-compatible API deployment."
description_source: auto
description_hash: af795fcc985a017a
id: 6b509205-dfb9-4527-986e-6d1bef6bbaf7
index_schema_version: 1
bdos_index: true
---
# Blackwell Server Setup for vLLM

This guide provides step-by-step instructions for setting up a Blackwell server to run vLLM with the MiniMax M2.1 model on Ubuntu 22.04.

## Prerequisites

- Ubuntu 22.04
- NVIDIA Blackwell GPU (e.g., B200, B100)
- Internet connection for downloading drivers and containers

## 1. NVIDIA Driver Installation

### Purge System
Start from a clean state by removing any previous NVIDIA installations:

```bash
sudo apt-get purge '*nvidia*'
sudo apt autoremove
```

### Install Prerequisites
Ensure all build tools and headers are present:

```bash
sudo apt update
sudo apt install linux-headers-$(uname -r) build-essential dkms
```

### Install the Correct Driver Variant
Install the `-open` version of the driver:

```bash
sudo apt install nvidia-driver-580-open
```

### Reboot
```bash
sudo reboot
```

### Verification
After rebooting, verify the installation:

```bash
nvidia-smi
```

You should see all device information displayed correctly.

## 2. Docker Installation

Install Docker using the official installation script:

```bash
curl -fsSL https://get.docker.com -o install-docker.sh
sudo sh install-docker.sh
sudo usermod -aG docker $USER
```

**Note**: Log out and back in for group changes to take effect, or use `newgrp docker`.

## 3. NVIDIA Container Toolkit Installation

Follow the official NVIDIA Container Toolkit installation guide:

### Install Prerequisites
```bash
sudo apt-get update && sudo apt-get install -y --no-install-recommends \
   curl \
   gnupg2
```

### Add NVIDIA Repository
```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

### Enable Experimental Features
```bash
sudo sed -i -e '/experimental/ s/^#//g' /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

### Update Package Lists
```bash
sudo apt-get update
```

### Install Specific Version
```bash
export NVIDIA_CONTAINER_TOOLKIT_VERSION=1.18.1-1
sudo apt-get install -y \
    nvidia-container-toolkit=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
    nvidia-container-toolkit-base=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
    libnvidia-container-tools=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
    libnvidia-container1=${NVIDIA_CONTAINER_TOOLKIT_VERSION}
```

### Configure Docker Runtime
Edit the Docker daemon configuration:

```bash
sudo vi /etc/docker/daemon.json
```

Add the following configuration:

```json
{
    "runtimes": {
        "nvidia": {
            "path": "nvidia-container-runtime",
            "runtimeArgs": []
        }
    }
}
```

Restart Docker to apply changes:

```bash
sudo systemctl restart docker
```

## 4. MiniMax M2.1 Setup

### Create Docker Compose Configuration
Create a `docker-compose.yaml` file:

```yaml
services:
  vllm:
    image: vllm/vllm-openai:nightly-da6709c9fe6965b7348692576ffadeee8439388e
    runtime: nvidia
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
    ports:
      - "8000:8000"
    volumes:
      - ./huggingface:/root/.cache/huggingface
    environment:
      HF_TOKEN: TBD
      SAFETENSORS_FAST_GPU: 1
    ipc: host
    command:
      - --model
      - MiniMaxAI/MiniMax-M2.1
      - --gpu_memory_utilization
      - "0.78"
      - --trust-remote-code
      - --tensor-parallel-size
      - "4"
      - --enable-auto-tool-choice
      - --tool-call-parser
      - minimax_m2
      - --reasoning-parser
      - minimax_m2_append_think
```

### Configuration Parameters Explained

- **image**: Uses the nightly build of vLLM with OpenAI compatibility
- **runtime**: Uses NVIDIA container runtime for GPU access
- **gpu_memory_utilization**: Allocates 78% of GPU memory
- **tensor_parallel_size**: Uses 4 GPUs for tensor parallelism
- **trust_remote_code**: Allows execution of remote code from the model
- **enable_auto_tool_choice**: Enables automatic tool selection
- **tool_call_parser**: Uses MiniMax M2 tool call parser
- **reasoning_parser**: Uses MiniMax M2 reasoning parser with thinking append

### Start the Service
```bash
docker compose up -d
```

## 5. Verification

Test the vLLM server by checking the available models:

```bash
curl localhost:8000/v1/models
```

You should receive a JSON response listing the MiniMax-M2.1 model.

## 6. API Usage

The server provides OpenAI-compatible API endpoints:

- **Chat Completions**: `POST /v1/chat/completions`
- **Completions**: `POST /v1/completions`
- **Embeddings**: `POST /v1/embeddings`
- **Models**: `GET /v1/models`

## Troubleshooting

### Check Container Logs
```bash
docker compose logs vllm
```

### Verify GPU Access
```bash
docker compose exec vllm nvidia-smi
```

### Monitor Resource Usage
```bash
watch -n 1 nvidia-smi
```

## Security Considerations

1. **HF_TOKEN**: Replace `TBD` with your actual Hugging Face token
2. **Network Security**: Consider implementing firewall rules to restrict access to port 8000
3. **Authentication**: Implement proper authentication for production use

## Performance Optimization

- Adjust `gpu_memory_utilization` based on your specific GPU memory
- Modify `tensor_parallel_size` based on the number of available GPUs
- Consider using model quantization for memory efficiency
- Monitor GPU utilization and adjust parameters accordingly

## Additional Resources

- [vLLM Documentation](https://docs.vllm.ai/)
- [NVIDIA Container Toolkit Documentation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/)
- [MiniMax AI Model Hub](https://huggingface.co/MiniMaxAI)