def sum_of_squares(a):
    num = 0
    for i in a:
        num += i*i
    return num

def test_one():
    assert sum_of_squares([1,2,3]) == 14