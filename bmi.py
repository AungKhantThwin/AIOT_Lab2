def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height * height)
    print("Bmi = " + str(bmi))

    status = ""
    if (bmi < 18.5):
        status = "Under Weight"
    elif (bmi >= 18.5 and bmi <= 25.0):
        status = "Normal Weight"
    else: 
        status = "Over Weight"
    print(status)


calculate_bmi(weight=57, height=1.73)