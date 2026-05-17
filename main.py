import os
from utils.parser import read_logs
from services.analyzer import filter_logs_by_status, count_log_statuses
from utils.file_handler import export_to_json

def main():
    """Main entry point for the Log Analyzer application."""
    print("--- Welcome to the Log Analyzer System ---")
    
    # Define paths
    log_file_path = "data/sample_logs.txt"
    export_file_path = "data/status_counts.json"
    
    # Check if data file exists
    if not os.path.exists(log_file_path):
        print(f"Error: Could not find the log file at '{log_file_path}'")
        return

    # 1. Load data using the generator from Participant 2
    print("Loading logs...")
    logs = list(read_logs(log_file_path))
    print(f"Successfully loaded {len(logs)} valid log entries.\n")

    # 2. Start the interactive menu
    while True:
        print("\n=== Main Menu ===")
        print("1. Filter logs by status (e.g., ERROR, INFO)")
        print("2. Count all log statuses")
        print("3. Export status counts to JSON")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            status = input("Enter status to filter: ").strip().upper()
            filtered = filter_logs_by_status(logs, status)
            
            print(f"\nFound {len(filtered)} logs with status '{status}':")
            # Show up to 5 logs so we don't flood the console
            for log in filtered[:5]: 
                print(log)
            if len(filtered) > 5:
                print(f"...and {len(filtered) - 5} more.")

        elif choice == '2':
            counts = count_log_statuses(logs)
            print("\nLog Status Counts:")
            for stat, count in counts.items():
                print(f"- {stat}: {count}")

        elif choice == '3':
            counts = count_log_statuses(logs)
            export_to_json(counts, export_file_path)
            print(f"\nSuccessfully exported status counts to '{export_file_path}'")

        elif choice == '4':
            print("\nExiting Log Analyzer. Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()