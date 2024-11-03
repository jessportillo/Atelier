from datetime import datetime, timedelta
import math

class AuditaData:
    def __init__(self, start_date: datetime, end_date: datetime):
        self.start_date = start_date
        self.end_date = end_date

    def getTotalTimeInMinutes(self):
        duration: timedelta = self.end_date - self.start_date
        total_minutes = duration.total_seconds() / 60.0
        return math.ceil(total_minutes)
    
    def __str__(self):
        return f"AuditaData: start_date: {self.start_date}, end_date: {self.end_date}"