name = input("what is your is name? ")
weight_kg = input("what is your weight in kg? ")
height_m = input("what is your height in meters? ")
height_m_sqr = float(height_m) * float(height_m)
bmi = float(weight_kg) / float(height_m_sqr)
roundBMI = round(bmi, 1)
print(roundBMI)
if bmi < 25:
    print(name + " is not overweight")
elif bmi == 25:
    print(name + " is borderline")
else:
    if bmi > 25:
        print(name + " is overweight")