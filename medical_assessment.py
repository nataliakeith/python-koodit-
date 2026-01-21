gender = str(input("Enter the gender: "))
hemoglobin = float(input("Enter the hemoglobin (g/l): "))
if gender == "male":
    if hemoglobin < 134:
        print("Hemoglobin is low.")
    elif hemoglobin > 167:
        print("Hemoglobin is high.")
    else:
        print("Hemoglobin is normal.")
if gender == "female":
    if hemoglobin < 117:
        print("Hemoglobin is low.")
    elif hemoglobin > 155:
        print("Hemoglobin is high.")
    else:
        print("Hemoglobin is normal.")