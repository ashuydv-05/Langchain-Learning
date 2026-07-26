 
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel): 
    
    name : str = Field(max_length=50)

    name : str = Annotated[str,Field(max_length=50,title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['ashu','priti'])]
    email : EmailStr
    age : int = Field(gt=0,lt=120)
    linkedin_url : AnyUrl
    #ADDING CUSTOM DATA VALIDATION
    weight : Annotated[float,Field(gt =0, strict = True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    #making allergies OPTIONAL
    #allergies: List[str]
    allergies: Annotated[Optional[List[str]], Field(default=None,max_length=5)]
    contact_details: Dict[str,str]


patient_info = {  
    'name':'ashu',
    'email':'asuu@outlook.com',
    'age':2,
    'weight':34.5,
    'linkedin_url' : 'https://leetcode.com/u/ashuydv_05/',
    #'married' : 1,
    # 'allergies': ['pollen','dust'],
    'contact_details':{'email':'abc@gmail.com','phone':'23070123154'}
    }

patient1 = Patient(**patient_info)
 
def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print(patient.email)
    print('inserted')
    print(patient.linkedin_url)


insert_patient_data(patient1)


