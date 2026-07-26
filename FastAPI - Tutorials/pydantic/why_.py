
#WHY ARE WE USING PYDANTIC (DATA VALIDATION AND SETTING DEFAULT VALUE IF REQ)

#below is the example for the python datatype eroor

'''def insert_patient_data(name, age):
  print(name)
  print(age)
  print('inserted into database')
'''

#ERROR !! But nothg is there to point out the error and , value DB me insert hojayega
#insert_patient_data('ashu','two')


# FIRST SOLU - TYPE HINTING

'''def insert_patient_data(name: str, age: int):
  print(name)
  print(age)
  print('inserted into database')

insert_patient_data('ashi', 30)
'''
# above insert will work, along with , if bychance in age section i wrote '30' as str then also it will work, No ERROR will  be there 

#SO TILL NOW DATA VALIDATION HAVE NOT HAPPENED YET , which is perfect



# ANOTHER METHOD 
#YEAH !! IT WORKS, BUT THIS SOLUTION IS NOT SCABALE
'''def insert_patient_data(name:str ,age: int):
  if type(name) == str and type(age) == int:
    print(name)
    print(age)
    print('inserted into database')

  else: 
    raise TypeError('Incorrect datatype')
  
insert_patient_data('ansh',20)'''