from database import AnalyzeDatabase

# Inicializar o banco de dados
database = AnalyzeDatabase()

# Exibir o conteúdo de todas as tabelas
print("Vagas:", database.jobs.all())
print("Resumos:", database.resums.all())
print("Análises:", database.analysis.all())
print("Arquivos:", database.files.all())
