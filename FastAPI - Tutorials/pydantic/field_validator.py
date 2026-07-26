from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

#FIELD VALIDATOR FOR EMAIL 
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        
        valid_domains =['hdfc.com','icici.com']
        #ashuyadav@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a Valid domain')

        return value
    
# FIELD VALIDATOR FOR CAPTITAL NAME
#LIKE THIS WE CAN MAKE SO MANY COUSTOM FILED VAILDATOR
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    

    @field_validator('age', mode='before')
    @classmethod
    def validate_age(cls, value):
        if 0< value<100:
            return value
        else:
            raise ValueError('Age should be in btw 0 and 100')
        
     

patient_info = {
    'name': 'nitish',
    'email': 'abc@hdfc.com',
    'age': '30',
    'weight': 75.2,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        'phone': '2353462'
    }
}
patient1 = Patient(**patient_info)
 

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')
    print(patient.email)


insert_patient_data(patient1)


