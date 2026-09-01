import unittest

from smoke import smoke_status


class SmokeStatusTest(unittest.TestCase):
    def test_pass_result(self):
        self.assertEqual(smoke_status("build", True), "build: PASS")

    def test_fail_result(self):
        self.assertEqual(smoke_status("build", False), "build: FAIL")

    def test_strips_whitespace_from_name(self):
        self.assertEqual(smoke_status("  build\t\n", True), "build: PASS")


if __name__ == "__main__":
    unittest.main()
