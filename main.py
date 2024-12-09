import sys
from datetime import datetime
from modules.gui.gui import GUI
from models.audita.audita_data import AuditaData
from models.audita.audita_data_group import AuditaDataGroup
from models.filtering.audita_group_filter import AuditaGroupFilter
from modules.search.search import get_audita_files_paths
from modules.audita.audita import interpret_audita_files
from modules.filtering.filter import filter_audita_data_list
from PyQt5.QtWidgets import (
    QApplication
)
from typing import List

def main():
    app = QApplication(sys.argv)
    window = GUI(program_loop)
    window.show()
    sys.exit(app.exec_())

def program_loop(selected_folders: List[str], min_date: datetime, max_date: datetime):
    audita_file_paths: List[str] = get_audita_files_paths(selected_folders)
    audita_data_list: List[AuditaData] = interpret_audita_files(audita_file_paths)
    audita_data_group : AuditaDataGroup = filter_audita_data_list(audita_data_list, min_date, max_date)
    totalTimeInMinutes = audita_data_group.getTotalTimeInMinutes()
    return totalTimeInMinutes


if __name__ == "__main__":
    main()