from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# from dotenv import load_dotenv
# load_dotenv()
embedding = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
documents = [
    "Ashu is an smart and descent boy with good intellactual property",
    "Priti is girlfriends of ashu, who is the university toper of Symbiosis",
    "Tanay and vandan are the common friend of priti and ashu"

]
query="tell me about vandan"
dr_embedd = embedding.embed_documents(documents)
print("Here is the embedding of the documents")
print(dr_embedd)

qr_embedd = embedding.embed_query(query)
print("Here is the embedding of the query")
print(qr_embedd)

print("SIMILARITY AND COMMON VECTOR")
# print(cosine_similarity([qr_embedd], dr_embedd))
score=cosine_similarity([qr_embedd], dr_embedd)[0]

index, score = sorted(list(enumerate(score)), key= lambda x:x[1]) [-1]

print(query)
print(documents[index])
print("similarity score is ", score)



    

