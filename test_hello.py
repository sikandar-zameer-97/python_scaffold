# Continuous Integration
import unittest
from hello import add


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(add(2, 3), 5)


if __name__ == "__main__":
    unittest.main()

# If test passes, CI/CD pipeline continues
# If test fails, pipeline is blocked
