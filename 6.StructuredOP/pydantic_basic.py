from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class Student(BaseModel):
    # default value is set here

    name : str = 'ashu'
    age : Optional[int] = None
    email: EmailStr
    cgpa: Optional[float] = Field(gt=8,lt=10, default = 4, description=" Decimal" \
    "value representing the cgpa of the student")
    # cgpa: Optional[float] = None

# new_s= {'name':'ashu', 'age': '23','email': 'ashu@gmail.com', 'cgpa':'7.99'}
new_s= {'name':'ashu', 'age': '23','email': 'ashu@gmail.com'}
# new_s= {'name': 'Pritee'}
stud  = Student(**new_s)
stud_dict = dict(stud)
print(stud_dict['email'])
stud_json = stud.model_dump_json
print("below the is the JSON output format")
print(stud_json)