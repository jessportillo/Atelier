from datetime import datetime
from models.audita.audita_data import AuditaData

def main():
    # Test dates
    date_1: datetime = datetime(2023, 10, 1, 12, 0)
    date_2: datetime = datetime(2023, 10, 1, 14, 30)
    
    # Audita Data Creation
    audita_data_1: AuditaData = AuditaData(date_1, date_2)

    # Test for audita_data_creation
    print(f"Audita Data Total Time: {audita_data_1.getTotalTimeInMinutes()} minutes")

    print("Program!")

if __name__ == "__main__":
    main()