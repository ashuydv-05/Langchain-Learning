from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel
import json
app = FastAPI()

# CREATING PYDANTIC MODEL FOR DATA VALIDATION
class Patient(BaseModel):
  


#creating an function to load the data (JSON)
def load_data():
  with open('patients.json','r') as f:
    data = json.load(f)

  return data


#created an ROUTES for GET 
@app.get("/")
def hello():
  return {'message':'Patient Management System API'}

@app.get('/about')
def about():
  return {'message':'A fully functional API to manage your patient records'}


#creating new END POINT TO GET THE DATA OF ALL PATIENT
@app.get('/view')
def view():
  data = load_data()

  return data

#Creating new END POINT TO GET DETAIL OF SPECIFIC PATIENT

#here patient_id is the. PATH PARAMETRE
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB ', example='P001')):
  #load all the patients
  data = load_data()

  if patient_id in data:
    return data[patient_id]
 
 #we ADDED, HTTP EXCEPTION
  raise HTTPException(status_code=404,detail='Patient Not Found' )


# QUERY. PARAMETER STARTS

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='sort on the basis of height weight'), order: str = Query('asc', description='sort in asc or desc order')):

    valid_fields = ['height','weight','bmi']

    if sort_by not in valid_fields:
      raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc','desc']:
      raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    # load data
    data = load_data()

    sort_order = True if order =='desc' else False

    sorted_data = sorted(data.values(), key=lambda x:x.get(sort_by,0),reverse=sort_order)

    return sorted_data






