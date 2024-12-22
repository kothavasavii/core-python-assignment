def search_patients_by_disease(patients, disease):
    return [patient["Name"] for patient in patients if patient["Disease"].lower() == disease.lower()]

patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

search_disease = input("search_disease = ")
result = search_patients_by_disease(patients, search_disease)

print(f"Patients with {search_disease}: {result}")
