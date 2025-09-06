SAVE-TO: /02_Books/Lee Boonstra - Prompt Engineering/
FILES:
  - Prompt_Engineering_Lee_Boonstra_2024.md
  - 2025-01-18-pdf-1-TechAI-Goolge-whitepaper_Prompt Engineering_v4-af36dcc7a49bb7269a58b1c9b89a8ae1.pdf (if provided)

---
title: "Prompt Engineering"
author: "Lee Boonstra"
year: 2024
completed: "2025-08-31"
tags: [whitepaper, prompt‑engineering, AI, generative‑AI]
source: "Full text"
status: done
---

# Prompt Engineering — Lee Boonstra (2024)

## Context

- **Author bio:** Lee Boonstra (they/them) is a software engineer and tech lead at Google Cloud’s Office of the CTO.  They have been active in technology since 2007, working as a software engineer, prompt engineer, web developer, technical trainer and developer advocate.  After eight years at Google, Boonstra now leads innovation projects and is recognised as a keynote speaker on conversational and generative AI【430207101278293†L41-L49】.  They have published books for O’Reilly and Apress and wrote Google’s prompt‑engineering whitepaper【430207101278293†L55-L57】.
- **Historical context:** In September 2024 Google released a 69‑page whitepaper titled “Prompt Engineering” written by Lee Boonstra.  The whitepaper quickly circulated among AI practitioners and marketers, providing structured guidance on designing effective prompts for large language models (LLMs) like Gemini, GPT and other systems【762996086837941†L55-L60】.  The release coincided with the explosion of interest in generative AI and the emergence of prompt engineering as a core professional skill.
- **Genre & tradition:** Technical whitepaper / how‑to guide.  The document synthesises best practices from natural language processing research and hands‑on experimentation, positioning itself alongside prompt‑engineering guides from OpenAI and other AI companies.
- **Contrarian signal:** Many prompt‑engineering guides emphasise “secret tricks”; Boonstra advocates an iterative, experimental process that builds on clear roles, context and instruction, discouraging reliance on vague constraints【762996086837941†L75-L79】【398098317545734†L1982-L2003】.
- **Reception & influence:** The whitepaper has become a go‑to reference for developers and marketers.  Articles summarising it highlight its four‑part prompt structure (role, context, instruction, output format) and stress that prompt engineering is an ongoing process【762996086837941†L55-L80】.  It was widely shared in online communities and inspired derivative guides and videos.
- **Comparable works:** OpenAI’s “Best practices for prompt engineering,” Google’s own prompting guides, and open‑source frameworks like LangChain’s prompting guides.  Books such as *Programming the OpenAI API* and blog series like “Prompt Engineering for the Enterprise” complement the whitepaper.
- **Who should read:** Developers, data scientists, product managers, marketers and anyone crafting prompts for LLMs.  The whitepaper assumes basic familiarity with AI but provides step‑by‑step instructions and examples.

## Abstract (<300 words)

This whitepaper introduces “prompt engineering” — the process of designing high‑quality prompts that guide large language models to produce accurate, useful outputs.  It argues that while anyone can write a prompt, effective prompting requires understanding the model’s configuration (temperature, top‑K and top‑P sampling) and iteratively refining the input【398098317545734†L416-L448】.  Boonstra begins by explaining LLM output configuration (output length, sampling controls) and shows how temperature and top‑K/top‑P parameters influence randomness and creativity.  The paper then surveys major prompting techniques.  Zero‑shot prompting provides only a task description; when this fails, one‑shot and few‑shot prompting add examples for the model to imitate【398098317545734†L421-L497】.  System, contextual and role prompting establish the model’s “big picture,” supply task‑specific context and assign a persona to generate consistent responses【398098317545734†L581-L597】.  Advanced strategies include step‑back prompts, chain‑of‑thought, self‑consistency, tree‑of‑thought, ReAct (reasoning & acting), automatic prompt engineering and code‑oriented prompting.  Boonstra devotes a chapter to prompting for code, illustrating how to write, explain, translate and debug code through carefully structured prompts.  The final section offers best practices: provide examples (few‑shot prompts) to teach the model, keep prompts simple and clear, specify desired outputs explicitly, favour positive instructions over constraints, control token length and reuse prompts via variables【398098317545734†L1966-L2052】.  Throughout, tables and real‑world examples demonstrate how to document prompts, choose model parameters and iterate.  Boonstra concludes that prompt engineering is an experimental process and encourages readers to document attempts and collaborate with other prompt engineers.

## Chapter Outline (Deep Analysis)

### Introduction — Why prompt engineering matters

**Guiding question:** What is prompt engineering and why does it require intentional design?

**Expanded answer & key ideas:** The introduction defines a prompt as the input provided to an LLM, often accompanied by other modalities.  Everyone can write a prompt, but crafting effective prompts is complex because multiple factors influence the model’s response: the chosen model, its training data, configuration (temperature, top‑K, top‑P) and the wording, tone, structure and context of the prompt【398098317545734†L152-L163】.  Prompt engineering is therefore an iterative process; inadequate prompts lead to ambiguous or inaccurate outputs【398098317545734†L164-L167】.  Boonstra emphasises that by prompting models directly (via the API) users gain access to configuration parameters such as temperature【398098317545734†L176-L183】.

**Thesis statement:** Effective prompt engineering requires understanding how LLMs generate outputs and iteratively refining prompts to achieve desired results.

**Extended commentary:** The introduction demystifies LLMs: they are prediction engines that generate the next token based on previous tokens and training data【398098317545734†L192-L203】.  When we write a prompt, we set up a chain of token predictions; our role is to guide this chain to the desired output【398098317545734†L203-L211】.  Recognising the predictive nature of LLMs underscores why specificity and context are crucial.

**Skeptical challenge:** To what extent can prompt engineering compensate for limitations in model training data?  Does emphasising prompt design risk underestimating the importance of high‑quality data and fine‑tuning?

**Applications & implications:** Understanding the model’s configuration and prediction behaviour helps practitioners across domains — from coding assistance to marketing copywriting — craft prompts that reduce hallucinations and improve accuracy.

### LLM Output Configuration — Temperature, Top‑K and Top‑P

**Guiding question:** How do model parameters control randomness and output length?

**Expanded answer & key ideas:** This chapter explains that LLM output length can be controlled via token limits.  Sampling controls such as temperature, top‑K and top‑P govern how “creative” the model can be.  Low temperatures produce deterministic, conservative responses; higher values encourage diversity.  Top‑K restricts sampling to the K most probable tokens, while top‑P (nucleus sampling) selects from the smallest set of tokens whose cumulative probability exceeds P【398098317545734†L443-L449】.  Adjusting these parameters together influences the balance between creativity and coherence.  Boonstra illustrates recommended defaults (e.g., temperature 0.2, top‑P 0.95) and notes that the gemini‑pro defaults disable both top‑K and top‑P.

**Thesis statement:** Configuring temperature and sampling parameters is foundational to prompt engineering because they shape the model’s stochasticity and can make or break an application’s output quality.

**Extended commentary:** The discussion emphasises that output length must be considered when supplying examples in few‑shot prompts to avoid truncation; token limits may need to be increased for longer responses.  These considerations highlight the interplay between prompt design and API parameters.

**Skeptical challenge:** Are recommended parameter settings consistent across different models (Gemini vs GPT vs Claude), or do they require experimentation?  How do safety filters interact with sampling settings?

**Applications & implications:** Model configuration is critical for tasks ranging from creative writing (higher temperature) to code generation (lower temperature for deterministic behaviour).

### Prompting Techniques — Zero‑Shot, One‑Shot & Few‑Shot

**Guiding question:** What are the basic prompting methods and when should they be used?

**Expanded answer & key ideas:** Zero‑shot prompting provides only a task description; it is the simplest form and works best when the task is straightforward【398098317545734†L421-L427】.  Boonstra demonstrates a zero‑shot sentiment‑classification prompt and emphasises the importance of documenting prompts and iterating【398098317545734†L430-L441】.  One‑shot prompting adds a single example for the model to imitate, while few‑shot prompting includes multiple examples (often three to five) to demonstrate patterns【398098317545734†L489-L509】.  The number of examples depends on task complexity and input length limitations【398098317545734†L501-L509】.

**Thesis statement:** Examples act as a powerful teaching signal for LLMs; when zero‑shot prompts fail, one‑shot and few‑shot strategies dramatically improve model performance.

**Extended commentary:** The examples illustrate how to structure tasks like classifying movie reviews or parsing pizza orders into JSON.  Using a table to document goal, model, temperature, token limit and prompt fosters reproducibility and collaboration among prompt engineers.  The best examples are relevant, diverse, high‑quality and include edge cases【398098317545734†L567-L575】.

**Skeptical challenge:** Do few‑shot examples risk leaking proprietary data or biasing the model if examples are poorly chosen?  How can we ensure fairness when selecting edge cases?

**Applications & implications:** Few‑shot prompting is widely used for tasks like question‑answering, classification and data extraction.  It allows users to adapt general models to domain‑specific tasks without fine‑tuning.

### System, Contextual & Role Prompting

**Guiding question:** How can prompt structure influence the model’s behaviour?

**Expanded answer & key ideas:** System prompting sets the overarching purpose for the model (e.g., translation or classification), contextual prompting adds background information relevant to a task, and role prompting assigns a persona or identity (e.g., act as a travel guide or marketing consultant)【398098317545734†L581-L597】.  These techniques help LLMs understand what to do and how to behave.

**Thesis statement:** A well‑structured prompt — clearly defining role, context and system purpose — produces more reliable and on‑brand outputs.

**Extended commentary:** Boonstra’s guidance aligns with the four‑part prompt structure summarised by marketing commentators: role, context, instruction and output format【762996086837941†L95-L104】.  Role prompting ensures the model adopts a consistent voice; contextual prompting reduces hallucinations by grounding the task; system prompts establish boundaries.

**Skeptical challenge:** Could excessive role‑playing lead to anthropomorphism or unrealistic expectations of the model’s capabilities?  What happens when multiple roles or contexts are mixed?

**Applications & implications:** System, contextual and role prompts are essential for professional applications like legal analysis (assign role: attorney), creative story generation (role: novelist), or customer support chatbots (context: company policies).

### Advanced Techniques — Chain‑of‑Thought, ReAct, ToT & Automatic Prompt Engineering

**Guiding question:** How do advanced prompting strategies improve reasoning and decision‑making?

**Expanded answer & key ideas:** Boonstra introduces step‑back prompting, chain‑of‑thought (CoT), self‑consistency, tree‑of‑thought (ToT) and ReAct.  In CoT, the model is encouraged to reason step by step; the whitepaper notes that CoT is low‑effort yet effective and can be combined with zero‑shot or few‑shot prompting【398098317545734†L55-L63】.  Self‑consistency samples multiple CoT responses and selects the most consistent answer.  ToT explores multiple reasoning paths to improve solution quality.  ReAct (Reason & Act) prompts the model to interleave reasoning with action, useful in agentic frameworks (e.g., LangChain)【398098317545734†L55-L63】.  Automatic prompt engineering leverages tools to generate and evaluate prompts programmatically.

**Thesis statement:** Advanced prompting techniques harness the reasoning capabilities of LLMs and enable complex tasks by encouraging structured thinking and iteration.

**Extended commentary:** These techniques are especially powerful for tasks like math problem solving, code generation and games.  They reflect a broader trend toward integrating reasoning frameworks with LLMs.

**Skeptical challenge:** Do multi‑step reasoning prompts introduce longer latency and cost?  How reliable are the model’s self‑evaluations when choosing the “best” reasoning path?

**Applications & implications:** Chain‑of‑thought and ReAct have been used to boost performance on reasoning benchmarks and to build conversational agents that can take actions (e.g., calling APIs).  Automatic prompt engineering suggests a future where tools can search the prompt space automatically.

### Code Prompting and Multimodal Considerations

**Guiding question:** How should prompts be structured for code‑related tasks and multimodal inputs?

**Expanded answer & key ideas:** The whitepaper dedicates a section to prompting for code — writing, explaining, translating and debugging.  It highlights using structured input and specifying output formats (e.g., JSON) to guide the model.  For multimodal prompting (text combined with images, audio or code), Boonstra notes that it is a separate concern: models like Gemini can accept multiple modalities, and prompts should specify each modality’s role【398098317545734†L1950-L1959】.

**Thesis statement:** Code and multimodal prompting share the same core principles as text prompting — clarity, structure and examples — but require attention to input formats and model capabilities.

**Extended commentary:** Multimodal prompting opens possibilities in domains like audio transcription, image captioning and code review.  The whitepaper emphasises that multimodal capabilities depend on model support; thus, prompt engineers should choose models accordingly.

**Skeptical challenge:** How mature are current multimodal models for complex tasks?  What safeguards are needed when mixing modalities (e.g., images containing sensitive data)?

**Applications & implications:** Developers can use these techniques to build interactive programming assistants, code translators and cross‑modal creative tools.

### Best Practices for Prompt Engineering

**Guiding question:** What practical guidelines can help practitioners design effective prompts?

**Expanded answer & key ideas:** Boonstra outlines a series of best practices:

1. **Provide examples.**  Few‑shot examples act as powerful teaching signals, improving accuracy, style and tone【398098317545734†L1966-L1974】.
2. **Design with simplicity.**  Prompts should be concise, clear and easy to understand; complex language or unnecessary information confuses both the human and the model【398098317545734†L1982-L1988】.  Using action verbs (“act,” “generate,” “summarize”) clarifies intent【398098317545734†L1996-L2003】.
3. **Be specific about the output.**  Clear instructions about desired length, style and structure help the model focus on relevant details【398098317545734†L2008-L2019】.
4. **Use instructions over constraints.**  Positive instructions tell the model what to do, while constraints specify what to avoid; positive framing is more effective and reduces confusion【398098317545734†L2022-L2052】.
5. **Control max token length.**  Set token limits or explicitly request output length to prevent truncation【398098317545734†L2072-L2077】.
6. **Use variables in prompts.**  Replace repeated text with variables to reuse prompts and integrate them into applications【398098317545734†L2078-L2101】.
7. **Experiment with input formats and writing styles.**  Try different prompt structures, writing styles and input formats; iterate and document attempts (the whitepaper suggests maintaining a prompt log).

**Thesis statement:** Prompt engineering excellence arises from discipline and experimentation: clear examples, specificity, positive instructions, token management and systematic documentation form the backbone of effective practice.

**Extended commentary:** The best‑practice section encourages readers to use tools like Vertex AI’s Language Studio to experiment with different models and prompts【398098317545734†L1961-L1964】.  It stresses that prompt engineering is not a one‑off act but an iterative process requiring collaboration and documentation — echoing the whitepaper’s overarching theme.

**Skeptical challenge:** How can prompt engineers systematically manage prompt revisions and experiments at scale?  Are there tools to version prompts and measure performance?

**Applications & implications:** These best practices have immediate utility for anyone building AI applications.  They can reduce failure modes, improve reliability and support governance of generative‑AI systems.

## Key Insights (7–10 notes)

1. **Prompts determine outcomes.**  Effective prompt engineering recognises that LLMs are prediction engines; clear roles, context and instructions steer the model toward desired outputs【398098317545734†L152-L163】.
2. **Model configuration matters.**  Temperature, top‑K and top‑P settings influence creativity and randomness; controlling them is essential for balancing determinism and diversity【398098317545734†L443-L449】.
3. **Examples teach the model.**  Zero‑shot prompts offer only a task description, while one‑shot and few‑shot prompts provide demonstrations that greatly improve performance【398098317545734†L421-L497】.
4. **Structured prompts boost reliability.**  Defining a system purpose, providing context and assigning a role produce more consistent and on‑brand responses【398098317545734†L581-L597】.
5. **Chain‑of‑thought and other advanced techniques unlock reasoning.**  Encouraging step‑by‑step reasoning and exploring multiple thought paths improves the quality of complex tasks【398098317545734†L55-L63】.
6. **Simplify and specify.**  Concise language, action verbs and explicit output instructions reduce ambiguity and help the model focus on relevant details【398098317545734†L1982-L1999】【398098317545734†L2008-L2019】.
7. **Positive instructions beat constraints.**  Telling the model what to do is more effective than listing what not to do; constraints should be used sparingly for safety and formatting【398098317545734†L2022-L2052】.
8. **Document and iterate.**  Prompt engineering is iterative; keeping a structured log of prompt attempts and results enables collaboration and continuous improvement【398098317545734†L430-L441】.
9. **Use variables and control token length.**  Variables make prompts reusable in applications, and setting token limits prevents truncation【398098317545734†L2072-L2101】.
10. **Choose the right model.**  Different LLMs may require different prompt configurations; experimentation is necessary to identify the best settings for each task.

## Suggested Atomic Notes (titles + one‑line summaries)

- **LLM Output Configuration** – Explains how temperature, top‑K and top‑P parameters control randomness and output length.
- **Zero‑Shot vs Few‑Shot Prompting** – Describes the spectrum from simple task descriptions to prompts with multiple examples.
- **System, Contextual & Role Prompts** – Summarises the four‑part structure (role, context, instruction, output format) that guides LLM behaviour.
- **Chain‑of‑Thought & Advanced Techniques** – Outlines reasoning‑based prompting methods like CoT, ReAct and tree‑of‑thought.
- **Prompt Engineering Best Practices** – Lists guidelines including providing examples, designing prompts with simplicity, being specific, using positive instructions, managing tokens and variables.
- **Code Prompting & Multimodal** – Highlights strategies for writing, explaining and translating code, and introduces multimodal prompting considerations.

## Suggested Contrast Notes

- **Prompt Engineering vs. OpenAI Best Practices** – Compare Boonstra’s guidelines with OpenAI’s prompt‑engineering recommendations to highlight similarities (e.g., clear instructions) and differences (e.g., emphasis on positive instructions over constraints).
- **Prompt Engineering vs. LangChain Prompt Templates** – Contrast the whitepaper’s manual iteration process with automated prompt‑template frameworks in tools like LangChain.

## Citations

1. Lee Boonstra’s biography describing their career at Google and their expertise in conversational and generative AI【430207101278293†L41-L49】.
2. Boonstra’s publications and mention of writing the Google Prompt Engineering whitepaper【430207101278293†L55-L57】.
3. Marketing article summarising the whitepaper and highlighting the four‑part prompt structure and iterative nature of prompt engineering【762996086837941†L55-L80】【762996086837941†L95-L104】.
4. Definition of prompt engineering and the factors influencing prompt effectiveness from the whitepaper【398098317545734†L152-L163】.
5. Explanation that prompt engineering is iterative and poor prompts lead to ambiguous or inaccurate outputs【398098317545734†L164-L167】.
6. Description of zero‑shot prompting and importance of documentation and iteration【398098317545734†L421-L441】.
7. Definitions of one‑shot and few‑shot prompting and guidance on the number of examples【398098317545734†L489-L509】.
8. Explanation of system, contextual and role prompting【398098317545734†L581-L597】.
9. Best‑practice guidance to provide examples, design prompts with simplicity and use action verbs【398098317545734†L1966-L1999】.
10. Recommendations to be specific about output and use positive instructions instead of constraints【398098317545734†L2008-L2052】.