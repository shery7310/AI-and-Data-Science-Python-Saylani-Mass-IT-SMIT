## What are Agents

Agents in essence are Large Language Models that accomplish a specific task.

Agents can be supplemented with tools, structured outputs and can hand-off to the other agents. 

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


![Prompt Chaining Diagram](https://raw.githubusercontent.com/shery7310/AI-and-Data-Science-Python-Saylani-Mass-IT-SMIT/main/Agents%20and%20Workflows/Prompt%20Chaining%20Diagram.png)

Output of LLM1 is going to a Gate which could be a **our** custom code which is optional, then based on some condition it could 
go to LLM2 and then LLM2's output could go to LLM3.

Or 

In other words we are chaining a series of fixed LLM calls decomposing into a fixed set of subtasks, then through each process we can set a guardrail (to ensure best outputs by LLMs) and do stuff. 

Here we can see that LLMs are somewhat driving their own processes so there is some autonomous stuff going on. 

##### 2. Routing

Direct and input into a specialized sub-task, ensuring separation of concerns

![](https://i.ibb.co/bgHbNQzZ/image.png)

Here the Router(orchestrator/triage LLM) will decide which of the 3 LLMs is best for a task and assign them the task as required. Different llms can have different expertise and usages.

Here the router is making decision so this means there is a lot of autonomy, and instead of relying on code we are relying on Router's decision, but since it still has to follow a given workflow this is why anthropic has labelled it as a given workflow.

##### 3. Parallelization

Breaking down tasks and running multiple sub-tasks concurrently. 

![](https://i.ibb.co/cSKBfJds/image.png)

Here the coordinator is our code deciding how to coordinate and how to assign code to LLMs, instead of an LLM orchestrating, and it can be sent in parallel to 3 or more LLMs to carry out 3 different activities and then the aggregator (which is again our code) concurrently takes the results from LLMs and concatenates a result for example a dictionary or some meaningful result. 

Anthropic suggests that we might even be giving the same task to three different LLMs for various reasons and let's aggregate the result and compare or use them later. 

##### 4. Orchestrator Worker

Challenging tasks are broken down and recombined.

![](https://i.ibb.co/Z6hTmJfR/image.png)

These seems same as the previous one but here our written code is not doing orchestration instead an LLMs is doing that. 

Essentially the model is breaking down a complex task into simpler tasks, then handing off to LLMs and then another LLM is combining the results. 

Again it won't be a good approach to categorize this a workflow as it seems more like an agent pattern. 

##### 5. Evaluator Optimizer

LLM output is validated by another.

![](https://i.ibb.co/0pn1fXvk/image.png)

Here we are using LLM as a judge (as openai agents documentation suggests). Let's say an LLm generates an output, the LLM Evaluator will check the output and reject it or keep it based on some condition which again is autonomous in this case and when the Evaluator LLM is satisfied only then the output will be accepted and shown to user. The LLM Evaluator can give feedback to LLM Generator aswell that this is what I am looking for, output this. 

This is a powerful way to increase accuracy of LLMs and it is mostly used, it is an effective pattern. 

Agents are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. 

Agents in comparison to workflows are:

Agents have feedback loops they are designed in a way that allows information to comeback and be processed multiple times. 

Unlike workflows agents don't have a fixed path or series of steps that needed to be followed, it's fluid but is more autonomous.

So such a system can lack things like guardrails, robustness and whether this fixes user's problems or not. 

We are to ensure best practices and usages to get the best out such a system. 

![](https://i.ibb.co/MDMB7zVn/image.png)

This is a very abstract diagram but it's saying the human inputs something to the LLM based on that the LLM performs an action on an environment for example another computer, and then after performing or confirming the task the LLM then brings back some feedback from the environment. 

This in comparison to work flows is way more fluid where LLMs can basically plot their own paths, but this can have many other issues.

Such as how long the agent will take to complete a task or it will even complete it's task at all, what kind of quality we are getting since there are no guardrails, how many tokens are being used (LLM api providers charge by tokens.

#### Risk of Agent Frameworks

##### Paths are unpredictable

We don't know which order tasks will take place or even what tasks will happen.

##### Unpredictable Output

We can't predict the output since we don't know about the which order the tasks are happening, also no guarantee that output's gonna be good or even reasonable. 

Yes we are giving LLMs autonomy but it's not always a good approach. 

##### Unpredictable Costs

We have no idea how long it might take to solve a problem, so we don't know how much we will be charged for API usage. 

##### Ways to Deal with these uncertainties

One of the ways we can deal with this is by monitoring what's going on in each LLM call when using both agentic/workflow design patterns by using concepts such as tracing and using Guardrails. 

Guardrails ensure your agents behave safely, consistently and within your intended boundaries.
