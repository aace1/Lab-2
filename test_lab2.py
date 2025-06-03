import lab2

def test_find_min_max():
    inputlist = [2,4,6,8,9,7,5,3,1]
    expected = [1,9]
    result = []
    result = lab2.find_min_max(inputlist)
    assert(result == expected)



def test_calc_average():
    inputlist = [2,4,6,8,9,7,5,3,1]
    expected = 5.0000
    result = lab2.calc_average(inputlist)
    result = round(result,4)
    assert(result == expected)



def test_calc_median_temperature():
    inputlist = [2,4,6,8,9,7,5.3,3,10,1]
    expected = 5.6500
    result = lab2.calc_median_temperature(inputlist)
    result = round(result, 4)
    assert(result == expected)



