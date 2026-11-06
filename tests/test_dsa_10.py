from dsa.dsa_10 import rotate_left

def test_dsa_10 ():

    assert rotate_left("abcdef", 2) == "cdefab"
    assert rotate_left("abcdef", 6) == "abcdef"
    assert rotate_left("abcdef", 10) == "efabcd"
    assert rotate_left("", 3) == ""