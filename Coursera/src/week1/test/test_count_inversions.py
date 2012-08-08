'''
Created on Jul 19, 2012

@author: mmcdonald
'''
import unittest
from week1.count_inversions import count_inversions

class Test_Count_Inversions(unittest.TestCase):
    def runTest(self):
        tenReverseSorted = [10,9,8,7,6,5,4,3,2,1]
        expectedInversions = len(tenReverseSorted) * (len(tenReverseSorted) - 1) / 2
        actualInversions, mergeSorted = count_inversions(tenReverseSorted)
        
        print(actualInversions)
        print(mergeSorted)
        self.assertEqual(expectedInversions, actualInversions, "count_inversions returned invalid result!")
        
        self.assertEqual(0, count_inversions([])[0], "count_inversions returned invalid result!")
        self.assertEqual(0, count_inversions([1])[0], "count_inversions returned invalid result!")
        self.assertEqual(1, count_inversions([2,1])[0], "count_inversions returned invalid result!")
        self.assertEqual(4, count_inversions([4,3,40,30,400,300,4000,3000])[0], "count_inversions returned invalid result!")
        
if __name__ == '__main__':
    unittest.main()