from crewai import Agent, Task, Crew, Process, LLM

model = LLM(
    model="ollama/llama3.1:8b",
    base_url="http://localhost:11434"
)

researcher = Agent(
    role="Pesquisador Técnico",
    goal="Pesquisar e explicar temas técnicos com clareza",
    backstory="Você é um pesquisador técnico especializado em inteligência artificial, software e DevOps.",
    llm=model,
    verbose=True
)

task = Task(
    description="Explique em até 5 linhas o que é um sistema multiagente.",
    expected_output="Uma explicação objetiva e técnica em português.",
    agent=researcher
)

crew = Crew(
    agents=[researcher],
    tasks=[task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()

print(result)