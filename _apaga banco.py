from database import AnalyzeDatabase

# Inicializar o banco de dados
database = AnalyzeDatabase()

# Confirmar antes de apagar
confirm = input("Tem certeza de que deseja apagar todas as vagas? Digite 'sim' para confirmar: ")

if confirm.lower() == "sim":
    # Apagar todas as vagas
    database.jobs.truncate()
    database.resums.truncate()
    database.analysis.truncate()
    database.files.truncate()
    database.close()  # Salva as mudanças
    print("Todas as vagas foram apagadas com sucesso.")
else:
    print("Operação cancelada.")
