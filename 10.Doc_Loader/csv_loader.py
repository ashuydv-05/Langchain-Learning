from langchain_community.document_loaders import CSVLoader
loader = CSVLoader(file_path='Sample CSV file for importing contacts.csv')

data = loader.load()
# print(len(data))
print(data[0])
