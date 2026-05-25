from crewai import Agent, LLM

llm = LLM(
    model="ollama/qwen2.5-coder:7b",
    base_url="http://localhost:11434"
)

collector = Agent(
    role="Coletor de Notícias de Tecnologia",
    goal="Coletar notícias relevantes de tecnologia em fontes públicas",
    backstory="Especialista em curadoria de notícias de tecnologia, IA, cloud, DevOps, segurança e open source.",
    llm=llm,
    verbose=True
)

classifier = Agent(
    role="Classificador de Relevância",
    goal="Classificar notícias por categoria, impacto e nível de repercussão",
    backstory="Analista técnico com experiência em tendências de tecnologia e impacto de mercado.",
    llm=llm,
    verbose=True
)

summarizer = Agent(
    role="Resumidor Executivo",
    goal="Transformar notícias técnicas em resumos claros, objetivos e úteis",
    backstory="Editor técnico especializado em explicar temas complexos para líderes de tecnologia.",
    llm=llm,
    verbose=True
)

hot_news_detector = Agent(
    role="Detector de Hot News",
    goal="Identificar notícias quentes que estão repercutindo fortemente no mundo da tecnologia",
    backstory="Analista de tendências e impacto tecnológico.",
    llm=llm,
    verbose=True
)

weekly_editor = Agent(
    role="Editor do Resumo Semanal",
    goal="Criar um relatório semanal consolidado com as principais notícias de tecnologia",
    backstory="Editor-chefe de uma newsletter semanal de tecnologia.",
    llm=llm,
    verbose=True
)