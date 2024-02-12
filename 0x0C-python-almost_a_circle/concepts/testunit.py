#assert 5 * 4 == 19, "Should be 20"

# def test_case_one():
    
#     assert 5 * 10 == 50, "Should be 50"

# def test_case_two():
    
#     assert 5 * 50 == 250, "Should be 250"


# if __name__ == "__main__":
    
#     test_case_one()
#     test_case_two()
    
#     print("All tests passed!")

# class MyTestCase(unittest.TestCase):
    
#     def test_one(self):
        
#         self.assertTrue(10 > 5, "Should Be True")

# if __name__ == "__main__":
#     unittest.main()

import unittest

class MyTestCase(unittest.TestCase):
    
    def test_one(self):
        self.assertTrue(10 > 1, "Should Be True")
    
    def test_two(self):
        self.assertEqual(40 + 60, 100, "Should be 100")
    
    def test_three(self):
        self.assertGreater(100, 80, "Should be True")

if __name__ == "__main__":
    unittest.main()
