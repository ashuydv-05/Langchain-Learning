from langchain_community.document_loaders import WebBaseLoader

url ="https://www.flipkart.com/beauty-and-grooming/~cs-bgw9lcx16o/pr?sid=g9b&collection-tab-name=MF&pageCriteria=default&p%5B%5D=facets.fulfilled_by%255B%255D%3DF-Assured&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D299&PARAM=456789&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InNvdXJjZUNvbnRlbnRUeXBlIjp7InNpbmdsZVZhbHVlQXR0cmlidXRlIjp7ImtleSI6InNvdXJjZUNvbnRlbnRUeXBlIiwiaW5mZXJlbmNlVHlwZSI6IlNDVCIsInZhbHVlIjoiSUFEIiwidmFsdWVUeXBlIjoiU0lOR0xFX1ZBTFVFRCJ9fX19fQ%3D%3D&nnc=ZAJ00B2OS3JS_IAD&BU=Mixed"
loader= WebBaseLoader(url)
docs = loader.load()

print(len(docs))

print(docs)