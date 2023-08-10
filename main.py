# Patients table, program entry point

import PySimpleGUI as sg
import dataFunctions
import patientIntakeForm

# Patients table column titles
table_headings = [
  "First name", "Last name", "Date of birth", "Height", "Weight",
  "Is taking medication?"
]
# Patients table data
table_data = dataFunctions.convert_patients_to_table_data()


# Add new patient button pressed, display patient intake form
def press_add_patient_button(patients_window):
  was_save_successful = patientIntakeForm.display_intake_form()
  if was_save_successful:
    table_data = dataFunctions.convert_patients_to_table_data()
    patients_window["PATIENTS_TABLE"].update(values=table_data)


# Patients window stuff
patients_window_layout = [
  [sg.Text("All Patient Data"),
   sg.Button("Add new patient")],
  [sg.Table(headings=table_headings, values=table_data, key="PATIENTS_TABLE")]
]
patients_window = sg.Window("Patients List", patients_window_layout)

# Display patient window
while True:
  event, values = patients_window.read()
  if event == sg.WIN_CLOSED:
    break
  elif event == "Add new patient":
    press_add_patient_button(patients_window)
patients_window.close()

# Tic Tac Toe challenge layout
# layout = [
#   [sg.Text('X'), sg.Text('O'),sg.Text('X')],
#   [sg.Text('O'), sg.Text('X'),sg.Text('O')],
#   [sg.Text('O'), sg.Text('O'),sg.Text('X')]
# ]
