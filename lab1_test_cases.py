import unittest
from lab1 import get_max
from lab1 import reverse
from lab1 import search
from lab1 import fib
from lab1 import factorial_iter
from lab1 import factorial_rec

class TestCase(unittest.TestCase):
    def test_get_max(self):
        arr = [1,2,3,4,5]
        self.assertEqual(get_max(arr), 5)

    def test_get_max_empty(self):
        arr = []
        self.assertEqual(get_max(arr), None)

    def test_reverse(self):
        self.assertEqual(reverse("qweEerty"), "ytreEewq")
        self.assertEqual(reverse(""), "")

    def test_search(self):
        arr = [1,2,3,4,5]
        self.assertEqual(search(arr, 5), 4)
        arr = []
        self.assertEqual(search(arr, 5), None)

    def test_search_index_bounds(self):
        arr = [1,2,3,4,5]
        self.assertEqual(search(arr, 6), None)

    def test_fib(self):
        def fib_numbers(n):
            sequence = []
            for i in range(n+1):
                sequence.append(fib(i))
            return sequence

        #this will test your fib function by calling it multiple times
        self.assertEqual(fib_numbers(10),
                [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_fib_init_terms(self):
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)

    def test_fib_zero(self):
        self.assertEqual(fib(0), 0)

    def test_factorial(self):
        self.assertEqual(factorial_iter(3), 6)
        self.assertEqual(factorial_iter(3), factorial_rec(3))

    def test_factorial_lt2(self):
        self.assertEqual(factorial_iter(0), 1)
        self.assertEqual(factorial_iter(1), 1)
        self.assertEqual(factorial_rec(0), 1)
        self.assertEqual(factorial_rec(1), 1)

    # def test_factorial_1000(self):
    #     self.assertEqual(factorial_iter(1000), 0)
    #     self.assertEqual(factorial_rec(1000), 0)

def main():
    # execute unit tests
    unittest.main()

if __name__ == '__main__':
    # execute main() function
    main()
