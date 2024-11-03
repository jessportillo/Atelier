import sys
from datetime import datetime
from models.audita.audita_data import AuditaData
from models.audita.audita_data_group import AuditaDataGroup
from models.filtering.audita_group_filter import AuditaGroupFilter
from modules.gui.gui import GUI
from PyQt5.QtWidgets import (
    QApplication
)

def main():
    # # Test dates
    # date_1: datetime = datetime(2023, 10, 1, 12, 30)
    # date_2: datetime = datetime(2023, 10, 1, 14, 30)
    # date_3: datetime = datetime(2023, 10, 1, 15, 30)

    # # Filter test dates
    # min_date_1: datetime = datetime(2023, 10, 1, 12, 30)
    # max_date_2: datetime = date_3
    
    # # Audita Data Creation
    # audita_data_1: AuditaData = AuditaData(date_1, date_2)
    # audita_data_2: AuditaData = AuditaData(date_2, date_3)
    # audita_data_3: AuditaData = AuditaData(date_1, date_3)

    # audita_data_list = [audita_data_1, audita_data_2, audita_data_3]
    # audita_data_group_filter_1: AuditaGroupFilter = AuditaGroupFilter(min_date_1, max_date_2)

    # audita_data_group = AuditaDataGroup(audita_data_list, audita_data_group_filter_1)

    # # Test for audita_data_creation
    # print(f"Audita Data Total Time: {audita_data_1.getTotalTimeInMinutes()} minutes")
    # print(audita_data_1)
    # print(audita_data_group_filter_1)
    # print(audita_data_group)
    # print(audita_data_group.getTotalTimeInMinutes())
    # print("Program!")
    app = QApplication(sys.argv)
    window = GUI()
    window.show()
    sys.exit(app.exec_())
    


if __name__ == "__main__":
    main()