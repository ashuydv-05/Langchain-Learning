from pydantic import BaseModel, EmailStr,model_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient older than 60 must have emergency contact')
        return model


patient_info = {
    'name': 'nitish',
    'email': 'abc@hdfc .com',
    'age': '61',
    'weight': 75.2,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        'phone': '2353462',
        'emergency': '134234'
    }
}
patient1 = Patient(**patient_info)
 

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')
    print(patient.email)


insert_patient_data(patient1)


