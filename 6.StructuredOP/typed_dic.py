from typing import TypedDict

# defination of the dic
class Person(TypedDict):
    name:str
    age:int

new_person: Person = {'name': 'ashu', 'age':35}

print(new_person)