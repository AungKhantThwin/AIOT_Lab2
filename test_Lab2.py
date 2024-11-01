import Lab2

def test_find_min_max():
    input_arr = [1, 8, 19, 11]
    result = Lab2.find_min_max(input_arr)
    assert (result == [1, 19])

def test_calc_aveerage():
    input_arr = [10, 10, 20, 30]
    result = Lab2.calc_average(input_arr)
    assert(result == 17.5)

def test_calc_median_temperature():
    input_arr = [1, 2, 3, 4, 5]
    result = Lab2.calc_median_temperature(input_arr)
    assert(result == 3)

