# Recursion: list sum.

def sum_list(a_list):
    if len(a_list) == 0:
        return 0
    return a_list[0] + sum_list(a_list[1:])

def test_sum(a_list):
    expected = sum(a_list)
    total = sum_list(a_list)
    print("Testing sum of ", a_list, "is", expected)
    assert expected == total


test_sum([1, 2, 3, 4])
test_sum([])  # testing special case
test_sum([10])  # testing special case
