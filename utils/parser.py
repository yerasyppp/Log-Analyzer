import re
from models.log_entry import LogEntry

def read_logs(file_path):
    """
    Reads a log file line by line using a generator.
    Extracts date, status, and message using regular expressions.
    """
    # Regex pattern to match the specific log format
    pattern = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+([A-Z]+)\s+(.+)$")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            clean_line = line.strip()
            match = pattern.match(clean_line)
            
            if match:
                # Yields one parsed entry at a time to save memory
                yield LogEntry(date=match.group(1), status=match.group(2), message=match.group(3))