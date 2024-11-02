from datetime import datetime
from models.audita.audita_data import AuditaData
from models.filtering.audita_group_filter import AuditaGroupFilter

def main():
    # Test dates
    date_1: datetime = datetime(2023, 10, 1, 12, 0)
    date_2: datetime = datetime(2023, 10, 1, 14, 30)

    # Filter test dates
    min_date_1: datetime = datetime(2023, 10, 1, 12, 30)
    max_date_2: datetime = date_2
    
    # Audita Data Creation
    audita_data_1: AuditaData = AuditaData(date_1, date_2)

    audita_data_group_filter_1: AuditaGroupFilter = AuditaGroupFilter(min_date_1, max_date_2)

    # Test for audita_data_creation
    print(f"Audita Data Total Time: {audita_data_1.getTotalTimeInMinutes()} minutes")
    print(audita_data_1)
    print(audita_data_group_filter_1)

    print("Program!")

if __name__ == "__main__":
    main()