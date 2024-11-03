from typing import List
import os
import fnmatch

AUDITA_FILE_NAME = "audita"

def get_audita_files_paths(selected_folders: List[str]):
    audita_files_paths: List[str] = []
    for folder in selected_folders:
        for root, _, files in os.walk(folder):
            for matched_file in fnmatch.filter(files, AUDITA_FILE_NAME):
                matched_file_path = os.path.join(root, matched_file)
                if matched_file_path not in audita_files_paths:
                    audita_files_paths.append(matched_file_path)
    return audita_files_paths