class LogEntry:
    """Base class representing a single system log entry."""
    
    def __init__(self, date, status, message):
        """Initialize a new log entry with validation."""
        valid_statuses = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        
        
        if status not in valid_statuses:
            raise ValueError(f"Invalid log status: {status}. Must be one of {valid_statuses}")
            
        
        self._date = date
        self._status = status
        self._message = message
        
    @property
    def date(self):
        """Get the date of the log entry."""
        return self._date

    @property
    def status(self):
        """Get the status of the log entry."""
        return self._status

    @property
    def message(self):
        """Get the message of the log entry."""
        return self._message

    def __str__(self):
        """Default string representation of a log entry."""
        return f"[{self.date}] {self.status} - {self.message}"


class InfoLog(LogEntry):
    """Class representing an informational log."""
    
    def __init__(self, date, message):
        """Initialize InfoLog. Status is automatically set to INFO."""
        # Inheritance: using the parent's __init__ method
        super().__init__(date, 'INFO', message)

    def __str__(self):
        """Polymorphism: specific string format for informational logs."""
        return f"[INFORMATION: {self.date}] -> {self.message}"


class ErrorLog(LogEntry):
    """Class representing a standard error log."""
    
    def __init__(self, date, message):
        """Initialize ErrorLog. Status is automatically set to ERROR."""
        super().__init__(date, 'ERROR', message)

    def __str__(self):
        """Polymorphism: specific string format for errors."""
        return f"[ERROR: {self.date}] -> Please check: {self.message}"


class CriticalLog(LogEntry):
    """Class representing a critical system failure log."""
    
    def __init__(self, date, message):
        """Initialize CriticalLog. Status is automatically set to CRITICAL."""
        super().__init__(date, 'CRITICAL', message)

    def __str__(self):
        """Polymorphism: highly visible string format for critical alerts."""
        return f"[CRITICAL ALERT: {self.date}] -> URGENT: {self.message}"