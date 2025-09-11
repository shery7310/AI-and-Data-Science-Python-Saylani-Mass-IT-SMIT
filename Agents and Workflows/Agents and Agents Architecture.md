## Agentic Architecture

AI Agents are programs where **LLM outputs** control the **workflow**. 

This flow can be called Agentic AI"
- Multiple LLM Calls
- LLMs with the ability to use tools (Orchestration)
- An environment where LLMs can interact with each other
- A Planner to coordinate activities
- Autonomy (Essence of Agentic AI)

He talks of LLMs to be statistical language models that can be autonomous.

## Two types of Agentic Systems

### Workflows

Workflows are systems where LLMs and tools ar orchestrated through predefined code paths.

#### 5 Types of Workflow Design Patterns

#### Prompt-Chaining

Decomposing problem into fix sub-tasks.

![[Prompt Chaining Diagram.png]]

Output of LLM1 is going to a Gate which could be a custom code which is optional, then based on some condition it could 
go to LLM2 and then LLM2's output could go to LLM3.

### Agents

Agents are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. 