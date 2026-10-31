from homework.day_9 import rotate_left

def test_dsa_day_9():
    assert rotate_left("abcde", 2) == "cdeab"
    assert rotate_left("abcde", 7) == "cdeab"
    assert rotate_left("abcde", 10) == "abcde"
    assert rotate_left("", 3) == ""
    print("All Test Passed")

#print(test_dsa_day_9())