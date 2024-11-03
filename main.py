import sys
from datetime import datetime
from models.audita.audita_data import AuditaData
from models.audita.audita_data_group import AuditaDataGroup
from models.filtering.audita_group_filter import AuditaGroupFilter
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox,
    QFileDialog, QLabel, QHBoxLayout, QCalendarWidget, QListView,
    QAbstractItemView, QTreeView, QDateTimeEdit
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
    window = MultiDirectorySelector()
    window.show()
    sys.exit(app.exec_())

class MultiDirectorySelector(QWidget):
    def __init__(self):
        super().__init__()

        self.selected_directories = []
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.folder_label = QLabel("No folders selected")
        folder_button = QPushButton("Select Folders")
        folder_button.clicked.connect(self.select_folders)

        layout.addWidget(folder_button)
        layout.addWidget(self.folder_label)

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

    

if __name__ == "__main__":
    main()