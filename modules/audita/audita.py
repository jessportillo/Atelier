from typing import List
from models.audita.audita_data import AuditaData
from datetime import datetime
import re

TARGET = "started at"

def interpret_audita_files(audita_file_paths: List[str]):
    for audita_file_path in audita_file_paths:
        audita_data = open_audita_file_and_interpret(audita_file_path)
        print(audita_data)

def open_audita_file_and_interpret(audita_file_path: str) -> AuditaData:
    start_time: datetime = get_start_time(audita_file_path)
    print(start_time)

def get_start_time(audita_file_path: str) -> datetime:
    audita_start_line: str = ""
    with open(audita_file_path, "r") as f:
        for line in f:
            line: str
            if TARGET in line:
                audita_start_line = line
    date_match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3} -\d{4})', audita_start_line)

    if date_match:
        date_str: str = date_match.group(1)
        date_obj: datetime = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f %z')
    
    if not date_obj:
        raise ValueError("Start Date not found.")
    
    return date_obj

def get_end_time(audita_file_path: str) -> datetime:
    pass