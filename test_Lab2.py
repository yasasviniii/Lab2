
import lab2

print("Test_Lab2")

def test_find_min_max():
    result = []
    input_list = [16,25.4,32.3,27.6,30,18]
    test_list = [16, 32.3]
    result = lab2.find_min_max(input_list)
    assert (result == test_list)

def test_calc_average():
    input_list = [16,25.4,32.3,27.6,30,18]
    test = 24.883
    result = lab2.calc_average(input_list)
    assert (result == test)

def test_calc_median_temperature():
    input_list = [16,25.4,32.3,27.6,30,18]
    test = 26.5
    result = lab2.calc_median_temperature(input_list)
    assert (result == test)
