from fhir_parser import FHIR
import matplotlib.pyplot as plt
import pandas as pd

fhir = FHIR(endpoint='https://fhir.compositegrid.com:5001/api/')
patients = fhir.get_all_patients()

genders = []
ages = []

for patient in patients:
    if patient.gender == 'male':
        genders.append(0)
    else:
        genders.append(1)
    ages.append(patient.age())

data = {'sex': genders, 'age': ages}
df = pd.DataFrame(data)

df.groupby('sex')['age'].plot(title='Age Distribution By Gender', kind='kde')
plt.show()
