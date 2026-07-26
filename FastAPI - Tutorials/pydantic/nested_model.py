from pydantic import BaseModel


class Address(BaseModel):
      city: str
      state: str
      pin : str


class Patient(BaseModel):
      name: str
      age: str
      address: Address



address={
      'city': 'patna',
      'state': 'bihar',
      'pin':'801503'
}

address_1 = Address(**address)

patient = {
      'name':'Ashu',
      'age': '23',
      'address':address_1
}

patient_1 = Patient(**patient)


print(patient_1)
print(patient_1.address.city)