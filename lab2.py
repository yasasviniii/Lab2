
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    templst = []
    user_input = input("Enter your temperatures: ")
    temp_inputs = user_input.split(",")
    for i in temp_inputs:
        templst.append(float(i))
    return templst

def calc_average(values):
    total = 0
    for i in values:
        total += i
    average = total / len(values)
    print("Average temperature is: " + str(average))
    return average
def find_min_max(values):
    min = 100000
    max = -100000
    for i in values:
        if i < min:
            min = i
        if i > max:
            max = i
    minmax = [min, max]
    print("Minimum and maximum temperature is: " + str(minmax))
    return minmax
def calc_median_temperature(values):
    if len(values) % 2 == 0:
        median = (values[len(values)//2] + values[len(values)//2 - 1]) / 2
    else:   
        median = values[len(values)//2]
    print("Median temperature is: " + str(median))
    return median

display_main_menu()
temp_values = get_user_input()
average = calc_average(temp_values)
minmax = find_min_max(temp_values)
