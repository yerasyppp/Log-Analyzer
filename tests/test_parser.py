import unittest
import re

class TestLogParser(unittest.TestCase):
    def setUp(self):
        self.pattern = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+([A-Z]+)\s+(.+)$")

    def test_valid_log_line(self):
        log_line = "2026-05-16 10:15:30 ERROR Connection timeout"
        match = self.pattern.match(log_line)
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), "2026-05-16 10:15:30")
        self.assertEqual(match.group(2), "ERROR")
        self.assertEqual(match.group(3), "Connection timeout")

    def test_invalid_log_line(self):
        log_line = "This is just random text"
        match = self.pattern.match(log_line)
        self.assertIsNone(match)

if __name__ == '__main__':
    unittest.main()
