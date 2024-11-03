import sys
from datetime import datetime
from models.audita.audita_data import AuditaData
from models.audita.audita_data_group import AuditaDataGroup
from models.filtering.audita_group_filter import AuditaGroupFilter
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QDateTimeEdit, QFileDialog, QLabel, QListWidget
)
from PyQt5.QtCore import QDateTime

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
    window = GUISelectorApp()
    window.show()
    sys.exit(app.exec_())

class GUISelectorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Reimagined System")
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()

        # Folder selection
        self.folder_list = QListWidget()
        self.folder_button = QPushButton("Select Folders")
        self.folder_button.clicked.connect(self.select_folders)
        layout.addWidget(self.folder_list)
        layout.addWidget(self.folder_button)

        # DateTime selection
        self.start_label = QLabel("Start Date and Time:")
        self.start_datetime = QDateTimeEdit(self)
        self.start_datetime.setCalendarPopup(True)
        self.start_datetime.setDateTime(QDateTime.currentDateTime())

        self.end_label = QLabel("End Date and Time:")
        self.end_datetime = QDateTimeEdit(self)
        self.end_datetime.setCalendarPopup(True)
        self.end_datetime.setDateTime(QDateTime.currentDateTime())

        layout.addWidget(self.start_label)
        layout.addWidget(self.start_datetime)
        layout.addWidget(self.end_label)
        layout.addWidget(self.end_datetime)

        # Start Button
        self.start_button = QPushButton("Start")
        self.start_button.setEnabled(False)
        self.start_button.clicked.connect(self.start_action)
        layout.addWidget(self.start_button)

        # Connect slots to check if inputs are complete
        self.start_datetime.dateTimeChanged.connect(self.check_complete)
        self.end_datetime.dateTimeChanged.connect(self.check_complete)
        self.folder_list.itemSelectionChanged.connect(self.check_complete)

        self.setLayout(layout)

    def select_folders(self):
        folders = []
        while True:
            folder = QFileDialog.getExistingDirectory(self, "Select Folder", "", QFileDialog.ShowDirsOnly)
            if folder:
                folders.append(folder)
                self.folder_list.addItem(folder)
            else:
                break
        self.check_complete()

    def check_complete(self):
        # Enable start button only if folder(s) are selected and valid dates are set
        if self.folder_list.count() > 0 and self.start_datetime.dateTime() < self.end_datetime.dateTime():
            self.start_button.setEnabled(True)
        else:
            self.start_button.setEnabled(False)
    
    def start_action(self):
        print("Action!")

if __name__ == "__main__":
    main()