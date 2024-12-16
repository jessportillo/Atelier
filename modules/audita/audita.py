from typing import List
from models.audita.audita_data import AuditaData
from datetime import datetime, timedelta
import re

LOWER_EXTREMUM_THRESHOLD = timedelta(minutes=1)
HIGHER_EXTREMUM_THRESHOLD = timedelta(hours=4000)
DEFAULT_ASSIGNEMENT_DURATION = timedelta(minutes=1)
DATETIME_PATTERN = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3} [+-]\d{4}"

def interpret_audita_files(audita_file_paths: List[str]):
    audita_data_list: List[AuditaData] = []
    for audita_file_path in audita_file_paths:
        audita_data = open_audita_file_and_interpret(audita_file_path)
        audita_data_list.append(audita_data)
    return audita_data_list

def open_audita_file_and_interpret(audita_file_path: str) -> AuditaData:
    start_time: datetime = get_start_time(audita_file_path)
    end_time: datetime = get_end_time(audita_file_path)
    audita_data: AuditaData
    if check_for_extremums(start_time, end_time):
        audita_data = AuditaData(start_time, start_time + DEFAULT_ASSIGNEMENT_DURATION, audita_file_path)
    else:
        audita_data = AuditaData(start_time, end_time, audita_file_path)
    return audita_data

def check_for_extremums(start_time: datetime, end_time: datetime):
    duration: timedelta = end_time - start_time
    return duration < LOWER_EXTREMUM_THRESHOLD or duration > HIGHER_EXTREMUM_THRESHOLD

def get_start_time(audita_file_path: str) -> datetime:
    with open(audita_file_path, "r") as f:
        file_content = f.read()

    # Extraction of all the dates from the file
    date_matches = re.findall(DATETIME_PATTERN, file_content)
    if not date_matches:
        raise ValueError("Date introuvable dans le fichier.")

    # Convertion of the dates in datetimes
    parsed_dates = [datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f %z") for date_str in date_matches]

    # Return first date
    date_obj = min(parsed_dates)
    return date_obj

def get_end_time(audita_file_path: str) -> datetime:
    with open(audita_file_path, "r") as f:
        file_content = f.read()

    # Extraction of all the dates from the file
    date_matches = re.findall(DATETIME_PATTERN, file_content)
    if not date_matches:
        raise ValueError("Date introuvable dans le fichier.")

    # Convertion of the dates in datetimes
    parsed_dates = [datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f %z") for date_str in date_matches]

    # Return second date
    date_obj = max(parsed_dates)
    return date_obj