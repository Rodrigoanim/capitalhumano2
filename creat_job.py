import uuid
from models.job import Job
from database import AnalyzeDatabase

database = AnalyzeDatabase()

# Perguntar ao usuário os detalhes da vaga
name = input("Digite o nome da vaga: ")

activities = input("Digite as atividades principais da vaga: ")

prerequisites = input("Digite os pré-requisitos da vaga: ")

differentials = input("Digite os diferenciais da vaga: ")

# Criar o objeto da vaga
job = Job(
    id=str(uuid.uuid4()),
    name=name,
    main_activities=activities,
    prerequisites=prerequisites,
    differentials=differentials,
)

# Inserir no banco de dados
database.jobs.insert(job.model_dump())

print(f"Vaga '{name}' criada com sucesso!")
