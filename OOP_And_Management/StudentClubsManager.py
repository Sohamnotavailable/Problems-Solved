#class Club:
"""
Represents a student club.
Attributes:
name (str)
students (dict[int, str]): maps student ID to position
(e.g., ’President’, ’Member’, or None).
"""
#pass
#class StudentClubs:
"""
Management system for multiple student clubs.
Methods:
- add_club(club_name)
- add_student(club_name, student_id, position)
- remove_student(club_name, student_id)
- add_position(club_name, student_id, new_position)
- remove_position(club_name, student_id)
"""
#pass

from typing import Dict, Optional

class Club:
    
    def __init__(self, name: str):
        self.name = name
        self.students: Dict[int, str] = {}


class StudentClubs:
    
    def __init__(self):
        self.clubs: Dict[str, Club] = {}

    def add_club(self, club_name: str):
        if club_name not in self.clubs:
            self.clubs[club_name] = Club(club_name)

    def add_student(self, club_name: str, student_id: int, position: str):
        if club_name in self.clubs:
            self.clubs[club_name].students[student_id] = position

    def remove_student(self, club_name: str, student_id: int):
        if club_name in self.clubs and student_id in self.clubs[club_name].students:
            del self.clubs[club_name].students[student_id]

    def add_position(self, club_name: str, student_id: int, new_position: str):
        if club_name in self.clubs:
            self.clubs[club_name].students[student_id] = new_position

    def remove_position(self, club_name: str, student_id: int):
        if club_name in self.clubs and student_id in self.clubs[club_name].students:
            self.clubs[club_name].students[student_id] = None
