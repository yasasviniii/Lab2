def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/height**2
    return bmi


def classify_bmi(bmi):
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25:
        print("Normal weight")
    else:
        print("Overweight")
    return

def main():
    bmiout = calculate_bmi(weight=57, height=1.73)
    print(f"Your BMI is: {bmiout:.2f}")
    classify_bmi(bmiout)

bmiout=calculate_bmi(weight=57, height=1.73)
print(f"Your BMI is: {bmiout:.2f}")
classify_bmi(bmiout)