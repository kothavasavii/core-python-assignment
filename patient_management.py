def search_patients_by_disease(patients, disease):
    """Return a list of patient names who have the specified disease."""
    return [patient["Name"] for patient in patients if patient["Disease"].lower() == disease.lower()]

# Example patient records
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

# Search for patients with a specific disease
search_disease = input("search_disease = ")
result = search_patients_by_disease(patients, search_disease)

# Output the results
print(f"Patients with {search_disease}: {result}")
