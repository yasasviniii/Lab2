def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/height**2
    return bmi


def classify_bmi(bmi):
    if bmi < 18.5:
        print("Underweight")
        print("-1")
    elif 18.5 <= bmi < 25:
        print("Normal weight")
        print("0")
    else:
        print("Overweight")
        print("1")
    return

#def main():
#    bmiout = calculate_bmi(weight=60, height=1.50)
#    print(f"Your BMI is: {bmiout:.2f}")
#    classify_bmi(bmiout)

bmiout=calculate_bmi(weight=60, height=1.5)
print(f"Your BMI is: {bmiout:.2f}")
classify_bmi(bmiout)