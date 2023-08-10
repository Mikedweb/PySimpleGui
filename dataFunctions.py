# Data and data manipulation functions

from patient import Patient
from datetime import datetime

# List of patients for our initial table data
patients = [
  Patient("Nimish", "Narang", datetime(1990, 1, 6), 185, 90.3, True),
  Patient("Zenva", "Academy", datetime(2000, 5, 29), 200, 100.5, False),
  Patient("Foo", "Bar", datetime(1965, 10, 4), 174, 83.6, False)
]


# Converts each patient into a list of strings for our table data
def convert_patients_to_table_data():
  patients_data = []
  for patient in patients:
    strings = patient.convert_values_to_strings()
    patients_data.append(strings)
  return patients_data


# Validates the input and attemts to create a patient, returns True if patient created successfully and False otherwise
def try_to_create_patient(first_name, last_name, date_of_birth, height, weight, is_taking_medication):
  if len(first_name) < 2 or len(last_name) < 2 or date_of_birth == "" or height == "" or weight == "":
    return False
    
  try:
    date_of_birth = datetime.strptime(date_of_birth, '%Y/%m/%d')
    if date_of_birth > datetime.now():
      return False
      
    height = int(height)
    weight = float(weight)
    if height <= 0 or weight <= 0:
      return False
  
    patient = Patient(first_name, last_name, date_of_birth, height, weight, is_taking_medication)
    patients.append(patient)
    return True
  except:
    return False