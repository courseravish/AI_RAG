from pathlib import Path
from hello_llm import ask

Path("W1_package/docs/runs/01-what-is-rag_Model_52.txt").write_text(ask("What is RAG?"))

print (ask("How many gold medal India won in Asian Games 2026?"))
Path("W1_package/docs/runs/02-India-AsianGames2026_Model_52.txt").write_text(ask("How many gold medal India won in Asian Games 2026?"))

print ('\n')
#print (ask("Name three uses of vector databases."))
Path("W1_package/docs/runs/03-vector-db-uses_Model_52.txt").write_text(ask("Name three uses of vector databases."))
print ('\n')
#print (ask("Please provide review of Emeritus and IITM Advance certification course in Agentic AI and RAG."))


