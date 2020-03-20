from fhir_parser import FHIR
import matplotlib.pyplot as plt
import numpy as np

fhir = FHIR(endpoint='https://fhir.compositegrid.com:5001/api/')
patients = fhir.get_all_patients()

married = [0] * 8
single = [0] * 8
for patient in patients:
    age = patient.age()
    for i in range(8):
        if age > 15*i and age <= 15*(i+1):
            if str(patient.marital_status) == 'Married':
                married[i] += 1
            else:
                single[i] += 1

width=0.9
p1 = plt.bar(np.arange(8), single, width)
p2 = plt.bar(np.arange(8), married, width,
             bottom=single)

plt.ylabel('Count')
plt.title('Marital Status by Age')
plt.xlabel("Age Groups")
plt.xticks(np.arange(8), ('0-15', '16-30', '31-45', '46-60', '61-75', '76-90', '91-105', '106-120'))
plt.yticks(np.arange(0, 300, 25))
plt.legend((p1[0], p2[0]), ('Single', 'Married'))

plt.show()