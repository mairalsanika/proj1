# Simple Hospital Management System

patients = {}

while True:
    print("\nHospital Management System")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        disease = input("Enter Disease: ")

        patients[pid] = {"Name": name, "Disease": disease}
        print("Patient added successfully!")

    elif choice == "2":
        if not patients:
            print("No patient records found.")
        else:
            for pid, details in patients.items():
                print(f"ID: {pid}, Name: {details['Name']}, Disease: {details['Disease']}")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")