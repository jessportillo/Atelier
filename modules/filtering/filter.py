from typing import List
from models.audita.audita_data import AuditaData
from datetime import datetime
from models.filtering.audita_group_filter import AuditaGroupFilter
from models.audita.audita_data_group import AuditaDataGroup

def filter_audita_data_list(audita_data_list: List[AuditaData], start_date: datetime, end_date: datetime) -> AuditaDataGroup:
    audita_group_filter : AuditaGroupFilter = create_audita_group_filter(start_date, end_date)
    return AuditaDataGroup(audita_data_list, audita_group_filter)

def create_audita_group_filter(start_date: datetime, end_date: datetime) -> AuditaGroupFilter:
    return AuditaGroupFilter(start_date, end_date)