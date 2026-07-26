# pip install pydantic

# CREATING THE PYDANTIC SCHEMA MODEL 
from pydantic import BaseModel


class Patient(BaseModel): #PYDANTIC MODEL (blueprint)
    
    name : str
    age : int

#CREATING THE RAW DATA (DICT OR JSON)
patient_info = { 
    'name':'ashu',
    'age':2
    }

#OBJECT CREATED OVER HERE with name - patient_1
# (**) used to unpack the dictionary
# here checking happen, if everything is correct then only
#OBJECT IS CREATED (VALIDATION HAPPENS HERE)
patient1 = Patient(**patient_info)
 

#PASSING AN OBJECT OVER HERE
# DETAIL OF PARAMETER THAT ARE BEING PASSED
'''
 Yeha par hum , insert_patient_data(patient_1) bhi krskte the.
 abhi insert_patient_data(patient :Patient ) & insert_patient_data(patient_1) , dono ek hi object ka reference hai. but
 insert_patient_data(patient :Patient ) - ( : Patient) this indicates that , i need 'patient' object of the type Patient

 patient : Patient  --- THIS IS THE TYPE HINT
'''
def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')


insert_patient_data(patient1)


