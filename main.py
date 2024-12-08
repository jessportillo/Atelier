import sys
from datetime import datetime
from typing import List
import pytz
import inquirer
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
from models.audita.audita_data import AuditaData
from models.audita.audita_data_group import AuditaDataGroup
from models.filtering.audita_group_filter import AuditaGroupFilter
from modules.search.search import get_audita_files_paths
from modules.audita.audita import interpret_audita_files
from modules.filtering.filter import filter_audita_data_list

def get_directories() -> List[str]:
    selected_directories = []
    print("Enter the directories to process (use TAB for autocomplete, type 'done' to finish):")
    path_completer = PathCompleter(only_directories=True)

    while True:
        directory = prompt("Directory: ", completer=path_completer).strip()

        if directory.lower() == 'done':
            break
        elif directory:
            selected_directories.append(directory)
            print(f"Added: {directory}")
        else:
            print("Invalid input. Please try again.")

    return selected_directories

def get_date(prompt_message: str) -> datetime:
    default_timezone = pytz.timezone("America/New_York")
    while True:
        try:
            date_input = input(f"{prompt_message} (format: YYYY-MM-DD HH:MM): ").strip()
            naive_datetime = datetime.strptime(date_input, "%Y-%m-%d %H:%M")
            return default_timezone.localize(naive_datetime)  # Apply the default timezone
        except ValueError:
            print("Invalid date format. Please try again.")

def program_loop(selected_folders: List[str], min_date: datetime, max_date: datetime):
    print("Processing...")
    audita_file_paths: List[str] = get_audita_files_paths(selected_folders)
    audita_data_list: List[AuditaData] = interpret_audita_files(audita_file_paths)
    audita_data_group: AuditaDataGroup = filter_audita_data_list(audita_data_list, min_date, max_date)
    print(f"Total minutes: {audita_data_group.getTotalTimeInMinutes()}")

def main():
    print("Welcome to the Audita Command-Line Tool")

    # Get directories from the user
    selected_folders = get_directories()
    if not selected_folders:
        print("No directories provided. Exiting.")
        sys.exit(1)

    # Get start and end dates
    min_date = get_date("Enter the start date and time")
    max_date = get_date("Enter the end date and time")

    if min_date >= max_date:
        print("Start date must be before end date. Exiting.")
        sys.exit(1)

    # Run the program logic
    program_loop(selected_folders, min_date, max_date)

if __name__ == "__main__":
    main()