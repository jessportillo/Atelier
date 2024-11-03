from datetime import datetime

class AuditaGroupFilter:
    def __init__(self, min_date: datetime, max_date: datetime):
        self.min_date = min_date
        self.max_date = max_date

    def __str__(self):
        return f"AuditaGroupFilter: min_date: {self.min_date}, max_date: {self.max_date}"