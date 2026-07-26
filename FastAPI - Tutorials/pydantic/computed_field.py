
from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel): #PYDANTIC MODEL (blueprint)
    
    name : str
    age : int
    weight: float
    height: float
    # married: bool
    # allergies : List[str]
    # contact_details: Dict[str,str]
  

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height ** 2),2)
        return bmi
    



patient_info = { 
    'name':'ashu',
    'age':2,
    'weight': 69,
    'height': 1.55
    }

patient1 = Patient(**patient_info)
def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')
    print(patient.calculate_bmi)



insert_patient_data(patient1)


