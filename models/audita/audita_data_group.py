from models.audita.audita_data import AuditaData
from models.filtering.audita_group_filter import AuditaGroupFilter
from typing import List

class AuditaDataGroup:
    def __init__(self, audita_data_list: List[AuditaData], audita_group_filter: AuditaGroupFilter):
        self.filtered_audita_data_list = self.filter_audita_data_list(audita_data_list, audita_group_filter)

    def filter_audita_data_list(self, audita_data_list: List[AuditaData], audita_group_filter: AuditaGroupFilter) -> List[AuditaData]:
        filtered_audita_data_list: List[AuditaData] = []
        for audita_data in audita_data_list:
            if (audita_data.start_date >= audita_group_filter.min_date) and (audita_data.end_date <= audita_group_filter.max_date):
                filtered_audita_data_list.append(audita_data)
        return filtered_audita_data_list

    def getTotalTimeInMinutes(self) -> int:
        total_time_in_minutes = 0  # Initialize the variable
        for audita_data in self.filtered_audita_data_list:
            total_time_in_minutes += audita_data.getTotalTimeInMinutes()
        return total_time_in_minutes
    
    def __str__(self) -> str:
        string = "Audita Data Group:\n"
        for audita_data in self.filtered_audita_data_list:
            string += f"- {audita_data}\n"
        string += "End Audita Data Group"
        return string
