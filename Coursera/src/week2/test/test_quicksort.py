'''
Created on Jul 19, 2012

@author: mmcdonald
'''
import unittest
from week2.quicksort import quicksort

class Test_Quicksort(unittest.TestCase):
    def runTest(self):
        listsToSort = [
                        [],
                        [99],
                        [6,5,4,3,2,1],
                        [1,2,3,4,5,6],
                        [123,5768,-238239,-2,0,43359,8392,-387294],
                        [123,5849,57385,903,387590478,2843284,3749,942,983,135983],
                       ]
        
        for toSort in listsToSort:
            pythonSorted = sorted(toSort)
            
            self.assertEqual(pythonSorted, quicksort(toSort), "Quicksort returned invalid result!")

if __name__ == '__main__':
    unittest.main()