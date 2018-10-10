import unittest
import random

def gen(n):
    return [random.randint(-10000, 1000000) for i in range(n)]

# Use wrapper class to prevent this class being discovered by nosetest.
class Wrapper:
    class TestSort(unittest.TestCase):  # Class TestSort inherits from class TestCase of module unittest
        # this is an abstract method, which will be overrided bu subclass.
        def sortMethod(self, arr):
            pass

        def test_empty(self):
            emptyArr = []
            self.sortMethod(emptyArr)
            self.assertEqual(emptyArr, [], "sort an empty array should return an empty array")

        def test_singleElement(self):
            single = [1]
            self.sortMethod(single)
            self.assertEqual(single, [1])

        def test_repeatedElements(self):
            elem = 1
            repeated = [elem for i in range(5)]
            self.sortMethod(repeated)
            # sort method should not change the size of the array
            self.assertEqual(len(repeated), 5)

            # after sort, all element will be the same
            self.assertTrue(all([x == elem for x in repeated]))

        def test_sort(self):
            a = [2, 3, 1, 6, 7, 5, 4]
            self.sortMethod(a)
            self.assertEqual(a, [1, 2, 3, 4, 5, 6, 7])


        def test_randomInput(self):
            for i in range(10):
                n = random.randint(100, 1000)
                randomArr = gen(n)
                self.sortMethod(randomArr)
                for j in range(n-1):
                    if randomArr[j] > randomArr[j+1]: # test case fail, sortMethod is wrong
                        print(randomArr)
                        self.fail("sort method provide wrong result for random arr")


if __name__ == '__main__':
    unittest.main()
