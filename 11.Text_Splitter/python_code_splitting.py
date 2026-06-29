from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text ="""class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating an object
s1 = Student("Ashu", 20)

# Calling method
s1.display()
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language= Language.PYTHON,
    chunk_size = 100,
    chunk_overlap = 0,
    # separator= ''
)

result = splitter.split_text(text)
# print(len(result))
print(result)