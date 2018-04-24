"""
Lab 22 - Practice Problems
Problem 7: Write a function that returns True if a number within 10 of 100.
"""

import unittest

# Near 100 function - If number is between 90 and 110, return true. Otherwise return false.
def near_100(num):
    if num in range(90, 110):
        return True
    else:
        return False


# Prompt for two numbers.
input_num = int(input("Enter a number around 100: "))


# Pass numbers to function and print result.
print(near_100(input_num))


# unittest
class MyTest(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_100(self):
        self.assertTrue(near_100(100))
 
    def test_80(self):
        self.assertFalse(near_100(80))

    def test_word(self):
    	self.assertFalse(near_100('word'))
 
if __name__ == '__main__':
    unittest.main()
