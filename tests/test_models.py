import unittest
from models.log_entry import LogEntry, InfoLog, ErrorLog

class TestLogEntryModels(unittest.TestCase):
    """Test cases for OOP models in the Log Analyzer project."""

    def test_base_log_entry_creation(self):
        """Test if the base LogEntry object is created with correct attributes."""
        log = LogEntry("2026-05-16", "WARNING", "Disk space is low")
        
        self.assertEqual(log.date, "2026-05-16")
        self.assertEqual(log.status, "WARNING")
        self.assertEqual(log.message, "Disk space is low")

    def test_invalid_status_raises_error(self):
        """Test if providing an invalid status raises a ValueError (Edge Case)."""

        with self.assertRaises(ValueError):
            LogEntry("2026-05-16", "INVALID_STATUS", "This should fail")

    def test_info_log_polymorphism(self):
        """Test if InfoLog child class correctly formats its string output."""
        info = InfoLog("2026-05-16", "User successfully logged in")
        
        self.assertEqual(info.status, "INFO")
        self.assertEqual(str(info), "[INFORMATION: 2026-05-16] -> User successfully logged in")

    def test_error_log_polymorphism(self):
        """Test if ErrorLog child class correctly formats its string output."""
        error = ErrorLog("2026-05-16", "Database connection lost")
        
        self.assertEqual(error.status, "ERROR")
        self.assertEqual(str(error), "[ERROR: 2026-05-16] -> Please check: Database connection lost")

if __name__ == '__main__':
    unittest.main()
