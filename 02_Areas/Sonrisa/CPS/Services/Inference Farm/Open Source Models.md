## TODO
- [ ] Select open source models  📅 2025-09-08 

## Core models to consider 2025 August
### 1. **Qwen 3 Series (235B MoE / 22B active)**

- **License**: Apache 2.0
- **Variants**: 0.6B to 235B, including Qwen2.5-Coder
- **Strengths**: Multilingual (119 languages), hybrid thinking modes, 128K context
- **Best for**: Coding, Chat, General purpose

### 2. **DeepSeek V3 / R1**

- **V3**: 671B MoE (37B active) - coding excellence
- **R1**: Reasoning-focused variant
- **License**: MIT (V3), Custom (R1)
- **Strengths**: SOTA math/coding (90%+ on benchmarks), 128K context
- **Best for**: Coding Assistant, Complex reasoning

### 3. **LLaMA 3.3 70B Instruct**

- **License**: Custom (Meta, commercial with conditions)
- **Strengths**: 86.3% MMLU, mature ecosystem, excellent quantization
- **Performance**: 2500 tokens/s throughput capability
- **Best for**: Chat Interface, General purpose

### 4. **Gemma 3 Family (1B-27B)**

- **License**: Custom Google license
- **Variants**: 1B, 4B, 12B, 27B
- **Strengths**: Multimodal, 140+ languages, 128K context, edge-deployable
- **Best for**: API Integration, Resource-constrained deployments

### 5. **GPT-oss (120B/20B)**

- **License**: Apache 2.0
- **Released**: August 2025 (OpenAI's first open weights since GPT-2)
- **Strengths**: Strong reasoning, optimized for consumer GPUs
- **Best for**: API Integration, Reasoning tasks

### 6. **AM-Thinking-v1 (32B)**

- **Base**: Fine-tuned from Qwen2.5-32B
- **Performance**: 85.3 AIME 2024, 70.3 LiveCodeBench
- **Strengths**: Outperforms DeepSeek R1 on reasoning
- **Best for**: Coding, Mathematical reasoning



### 7. **Phi-3/Phi-4 Series (Microsoft)**

- **Sizes**: 3.8B-14B
- **License**: MIT
- **Strengths**: Exceptional efficiency, 62.2% HumanEval, low VRAM (~7GB INT4)
- **Best for**: API Integration, Edge deployment

### 8. **Mixtral Models (Mistral AI)**

- **8x7B**: Efficient MoE, 6x faster than dense equivalents
- **8x22B**: 141B total (39B active), 64K context
- **License**: Apache 2.0
- **Best for**: Production deployments, Chat

### 9. **Yi-1.5-34B**

- **License**: Apache 2.0
- **Strengths**: Strong bilingual (EN/Chinese), 32K context
- **Performance**: 78% MMLU, 75% HumanEval
- **Best for**: Multilingual applications, Coding

### 10. **CodeLlama 34B**

- **License**: Custom Meta license
- **Performance**: 75% HumanEval, 16K context
- **Strengths**: Purpose-built for code generation
- **Best for**: Coding Assistant


### 11. **Llama 4 Scout/Maverick**

- **Scout**: 109B total (17B active)
- **Maverick**: 400B total (17B active)
- **Context**: 10 million tokens (industry-leading)
- **Status**: Mixed early benchmarks, needs validation
- **Best for**: Experimental/cutting-edge applications

### 12. **Apertus (8B/70B)**

- **Origin**: European, ethically sourced
- **Claims**: 1,800+ languages support
- **License**: Fully open
- **Status**: New, limited independent validation

### 13. **Falcon 3 Series (7B/10B/40B)**

- **License**: TII Falcon 2.0 (permissive)
- **Strengths**: Multimodal capabilities (newer versions)
- **Note**: Falcon 180B is outdated; focus on Falcon 3

### 14. **Mistral 7B v0.3**

- **License**: Apache 2.0
- **Context**: 32K
- **Strengths**: Production-proven, function calling support
- **Best for**: Lightweight API integration



## Core dimensions to consider

| Dimension                       | Coding Assistant | Chat UI | API Integration |
| ------------------------------- | ---------------- | ------- | --------------- |
| **A.1 Multilingual Ability**    | 2                | 5       | 3               |
| **A.2 Coding Performance**      | 5                | 1       | 1               |
| **A.3 Reasoning Ability**       | 5                | 3       | 3               |
| **A.4 Instruction Following**   | 4                | 5       | 3               |
| **A.5 RAG-Friendliness**        | 2                | 3       | 5               |
| **A.6 Multimodal Support**      | 1                | 3       | 2               |
| **B.7 Context Window Size**     | 5                | 3       | 2               |
| **B.8 Model Size**              | 4                | 3       | 3               |
| **B.9 VRAM Footprint**          | 4                | 3       | 5               |
| **B.10 Quantization Quality**   | 4                | 3       | 5               |
| **B.11 Inference Speed**        | 4                | 5       | 5               |
| **B.12 Cold Start Time**        | 2                | 4       | 5               |
| **C.13 vLLM Compatibility**     | 2                | 3       | 5               |
| **C.14 Fine-tuning Support**    | 4                | 2       | 3               |
| **C.15 RAG Integration**        | 2                | 3       | 5               |
| **C.16 Streaming Support**      | 2                | 5       | 2               |
| **C.17 Prompt Format Standard** | 2                | 3       | 3               |
| **D.18 License Type**           | 4                | 3       | 3               |
| **D.19 Community & Tooling**    | 4                | 3       | 3               |
| **D.20 Benchmark Transparency** | 4                | 3       | 3               |





## Key Soruces
# Extended List of LLM Benchmarking Authorities with Links

## **Model Capabilities (A.1–A.6)**

### Primary Leaderboards

- **LMSYS Chatbot Arena** → https://chat.lmsys.org/?leaderboard
    
    - The _de facto_ leaderboard for reasoning, instruction-following, and multilingual quality based on crowd-sourced human preference judgments (Elo-style ranking)
    - Alternative view: https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard
- **Open LLM Leaderboard (HuggingFace)** → https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard
    
    - Evaluates on MMLU, HumanEval, GSM8K, TruthfulQA, ARC, HellaSwag
    - Version 2: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard
- **BigCode Leaderboard** → https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard
    
    - Focused authority for coding performance (HumanEval, MultiPL-E, DS-1000)
    - EvalPlus: https://evalplus.github.io/leaderboard.html
- **VLM/Multimodal Benchmarks**:
    
    - **OpenCompass MMBench** → https://mmbench.opencompass.org.cn/leaderboard
    - **MMMU Benchmark** → https://mmmu-benchmark.github.io/
    - **HuggingFace Vision Arena** → https://huggingface.co/spaces/opencompass/open_vlm_leaderboard

### Specialized Benchmarks

- **HELM (Stanford)** → https://crfm.stanford.edu/helm/latest/
- **AlpacaEval** → https://tatsu-lab.github.io/alpaca_eval/
- **MT-Bench** → https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge
- **RAGAS (RAG evaluation)** → https://docs.ragas.io/en/latest/

## **Performance & Deployment (B.7–B.12)**

### Model Information Sources

- **HuggingFace Model Hub** → https://huggingface.co/models
    
    - Individual model cards contain context window, parameters, VRAM requirements
    - Example format: https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct
- **vLLM Performance Benchmarks**:
    
    - **Official vLLM Docs** → https://docs.vllm.ai/en/latest/performance/benchmarks.html
    - **vLLM GitHub** → https://github.com/vllm-project/vllm
    - **Compatibility Matrix** → https://docs.vllm.ai/en/latest/models/supported_models.html
- **Quantization Resources**:
    
    - **llama.cpp** → https://github.com/ggerganov/llama.cpp
    - **ExLlamaV2** → https://github.com/turboderp/exllamav2
    - **AutoGPTQ** → https://github.com/AutoGPTQ/AutoGPTQ
    - **AutoAWQ** → https://github.com/casper-hansen/AutoAWQ
    - **GGUF Format Docs** → https://github.com/ggerganov/ggml/blob/master/docs/gguf.md

### Performance Testing

- **Artificial Analysis** → https://artificialanalysis.ai/models
    - Independent benchmarks of latency, throughput, pricing
- **Papers With Code** → https://paperswithcode.com/sota
    - State-of-the-art tracking across benchmarks
- **Reddit r/LocalLLaMA** → https://www.reddit.com/r/LocalLLaMA/
    - Community testing and real-world experiences

## **Engineering & Integration (C.13–C.17)**

### Framework Support

- **LangChain Documentation**:
    
    - **Model Support** → https://python.langchain.com/docs/integrations/llms/
    - **Chat Models** → https://python.langchain.com/docs/integrations/chat/
    - **LangChain Hub** → https://smith.langchain.com/hub
- **LlamaIndex Documentation**:
    
    - **LLM Support** → https://docs.llamaindex.ai/en/stable/module_guides/models/llms.html
    - **Integration Gallery** → https://llamahub.ai/
- **vLLM Compatibility**:
    
    - **Supported Models** → https://docs.vllm.ai/en/latest/models/supported_models.html
    - **Adding New Models** → https://docs.vllm.ai/en/latest/models/adding_model.html

### Fine-tuning & Training

- **Axolotl** → https://github.com/OpenAccess-AI-Collective/axolotl
    - Comprehensive fine-tuning framework support matrix
- **PEFT (HuggingFace)** → https://github.com/huggingface/peft
    - LoRA/QLoRA compatibility documentation
- **Unsloth** → https://github.com/unslothai/unsloth
    - Optimized fine-tuning support
- **LLaMA-Factory** → https://github.com/hiyouga/LLaMA-Factory
    - Multi-model fine-tuning support

### Deployment Tools

- **Ollama Model Library** → https://ollama.com/library
    - Pre-quantized models and deployment info
- **Text Generation Inference (TGI)** → https://github.com/huggingface/text-generation-inference
    - Production deployment specifications
- **OpenLLM** → https://github.com/bentoml/OpenLLM
    - Model serving compatibility

## **License & Ecosystem (D.18–D.20)**

### License Information

- **HuggingFace Model Licenses** → https://huggingface.co/docs/hub/model-cards#model-card-licenses
    - Comprehensive license database
- **Choose a License** → https://choosealicense.com/
    - Understanding open-source licenses
- **TLDRLegal** → https://tldrlegal.com/
    - Simplified license explanations

### Community & Activity Metrics

- **HuggingFace Trending** → https://huggingface.co/models?sort=trending
    - Downloads, likes, and activity metrics
- **GitHub Trending** → https://github.com/trending/python?since=monthly
    - Repository activity for ML projects
- **Google Scholar** → https://scholar.google.com/
    - Citation counts for model papers

### Benchmark Transparency

- **Open LLM Benchmark Results** → https://huggingface.co/datasets/open-llm-leaderboard/results
    - Raw evaluation data
- **EleutherAI Eval Harness** → https://github.com/EleutherAI/lm-evaluation-harness
    - Reproducible evaluation framework
- **BIG-bench** → https://github.com/google/BIG-bench
    - Comprehensive benchmark suite

## **Additional Authoritative Resources**

### Model Comparison Tools

- **LLM Arena (Comparative)** → https://arena.lmsys.org/
- **Perplexity Labs Playground** → https://labs.perplexity.ai/
- **Poe Model Comparison** → https://poe.com/

### Cost & Efficiency Analysis

- **LLM Price Calculator** → https://llm-price.com/
- **Token Counter** → https://platform.openai.com/tokenizer
- **GPU Benchmark Database** → https://lambdalabs.com/gpu-benchmarks

### Safety & Alignment

- **HELM Safety Metrics** → https://crfm.stanford.edu/helm/latest/?group=safety
- **TruthfulQA Leaderboard** → https://github.com/sylinrl/TruthfulQA
- **Anthropic Evals** → https://github.com/anthropics/evals

### Real-time Model Tracking

- **Hugging Face Daily Papers** → https://huggingface.co/papers
- **ArXiv CS.CL** → https://arxiv.org/list/cs.CL/recent
- **Model Index** → https://www.modelindex.org/

This comprehensive list provides direct access to authoritative sources for evaluating and comparing open-source LLMs across all critical dimensions for enterprise deployment decisions.