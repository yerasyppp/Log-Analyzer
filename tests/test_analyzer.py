import unittest
from models.log_entry import LogEntry
from services.analyzer import filter_logs_by_status, count_log_statuses


class TestAnalyzer(unittest.TestCase):

    def setUp(self):
        self.sample_logs = [
            LogEntry("2026-05-16", "INFO", "System boot initiated"),
            LogEntry("2026-05-16", "ERROR", "Failed to connect to database"),
            LogEntry("2026-05-16", "INFO", "Service started successfully")
        ]

    def test_filter_logs_by_status(self):
        filtered_logs = filter_logs_by_status(self.sample_logs, "INFO")

        self.assertEqual(len(filtered_logs), 2)
        self.assertEqual(filtered_logs[0].status, "INFO")
        self.assertEqual(filtered_logs[1].status, "INFO")

    def test_count_log_statuses(self):
        counts = count_log_statuses(self.sample_logs)

        self.assertEqual(counts.get("INFO"), 2)
        self.assertEqual(counts.get("ERROR"), 1)
        self.assertIsNone(counts.get("WARNING"))


if __name__ == '__main__':
    unittest.main()