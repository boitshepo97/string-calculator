import pytest
from string_calculator import add

def test_add_empty():
    #Question 1: Empty string
    assert add("") == 0

def test_add_one():
    #Question 1: One number
    assert add("1") == 1

def test_add_two():
    #Question 1: Two number
    assert add("1,10") == 11

def test_add_uknown_number():
    #Question 2: Unknown amount of numbers 
    assert add("1,2,3,4,5") == 15

def test_add_new_line():
    #Question 3.1: Test handling new lines
    assert add("1\n2,3") == 6

def test_add_new_line_error():
    #Question 3.2: Test handling new lines error
    assert add("1\n") == 1

def test_add_different_delimiters():
    #Question 4.1: Test support different delimiters
    assert add("//;\n1;2") == 3

def test_add_esisting_scenario():
    #Question 4.2: Test existing scenarios
    assert add("1;2;;1") == 4

def test_add_negatives():
    #Question 5: Test negative number will throw an exception "negatives not allowed"
    with pytest.raises(Exception) as error:
        assert add("-1,-1,2")
        str(error.value) == "negatives not allowed! -1, -1."

def test_add_bigger():
    #Question 6: Test numbers bigger than 1000 are ignored
    assert add("2+1001") == 2   

def test_add_any_length():
    #Question 7: Test delimiters of any length
    assert add("//[***]\n1***2***3") == 6  

def test_add_multiple():
    #Question 8: Test multiple delimiters of any length
    assert add("//[*][%]\n1*2%3") == 6   

def test_add_more_characters():
    #Question 9: Test multiple delimiters with length longer than one character   
    assert add("//[*][%]\n1*2%+???++@aqw^^^\\^3") == 6