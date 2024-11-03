from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QLabel, QListView,
    QAbstractItemView, QTreeView, QDateTimeEdit
)
from PyQt5.QtCore import QDateTime
from typing import Callable, List
from datetime import datetime

class GUI(QWidget):
    def __init__(self, program_loop: Callable[[List[str], datetime], None]):
        super().__init__()

        self.program_loop: Callable = program_loop
        self.selected_directories = []
        self.start_date = None
        self.end_date = None
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        #Folder selection
        self.folder_label = QLabel("No folders selected")
        folder_button = QPushButton("Select Folders")
        folder_button.clicked.connect(self.select_folders)

        layout.addWidget(folder_button)
        layout.addWidget(self.folder_label)

        #Start Datetime
        self.start_datetime_label = QLabel("Start Date & Time:")
        self.start_datetime_edit = QDateTimeEdit(self)
        self.start_datetime_edit.setCalendarPopup(True)
        self.start_datetime_edit.setDateTime(QDateTime.currentDateTime())

        self.start_datetime_edit.dateTimeChanged.connect(self.set_start_datetime)

        layout.addWidget(self.start_datetime_label)
        layout.addWidget(self.start_datetime_edit)

        #End Datetime
        self.end_datetime_label = QLabel("End Date & Time:")
        self.end_datetime_edit = QDateTimeEdit(self)
        self.end_datetime_edit.setCalendarPopup(True)
        self.end_datetime_edit.setDateTime(QDateTime.currentDateTime())

        # Connect the date-time change to update the selected end date
        self.end_datetime_edit.dateTimeChanged.connect(self.set_end_datetime)

        # Add to the layout
        layout.addWidget(self.end_datetime_label)
        layout.addWidget(self.end_datetime_edit)

        # Start Button
        self.start_button = QPushButton("Start")
        self.start_button.setEnabled(False)  # Initially disabled
        self.start_button.clicked.connect(self.start_program)
        layout.addWidget(self.start_button)
        
        self.setLayout(layout)
        self.setWindowTitle('Multi-Folder Selector')
        self.setGeometry(400, 200, 600, 400)

    def select_folders(self):
        dialog = QFileDialog(self, "Select Folders")
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setOption(QFileDialog.Option.DontUseNativeDialog, True)

        # Enable multiple selection
        list_view = dialog.findChild(QListView, "listView")
        if list_view:
            list_view.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        tree_view = dialog.findChild(QTreeView)
        if tree_view:
            tree_view.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        if dialog.exec() == QFileDialog.DialogCode.Accepted:
            self.selected_directories = dialog.selectedFiles()
            truncated_paths = [self.truncate_path(path) for path in self.selected_directories]
            self.folder_label.setText("Selected Folders:\n" + '\n'.join(truncated_paths))
        else:
            self.folder_label.setText("No folders selected")

    def truncate_path(self, path, max_length=95):
        # Truncate the path if it exceeds max_length, adding "..." in the middle
        if len(path) > max_length:
            return path[:15] + "..." + path[-80:]
        return path
    
    def set_start_datetime(self, datetime):
        self.start_date = datetime
        self.check_complete()

    def set_end_datetime(self, datetime):
        self.end_date = datetime
        self.check_complete()

    def check_complete(self):
        # Enable Start button only if all conditions are met
        if self.selected_directories and self.start_date and self.end_date and self.start_date < self.end_date:
            self.start_button.setEnabled(True)
        else:
            self.start_button.setEnabled(False)

    def start_program(self):
        # Logic to execute when the Start button is clicked
        print(f"Selected Directories: {self.selected_directories}")
        print(f"Start Date: {self.start_date}")
        print(f"End Data: {self.end_date}")
        self.program_loop(self.selected_directories, self.start_date, self.end_date)