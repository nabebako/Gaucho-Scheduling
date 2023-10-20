from .general_education import General_Education

class Course_Criteria:
    course_id: str
    course_name: str
    course_number: str
    college: str
    general_edu: [General_Education]
    is_perference: bool # is_perfernece means that the course could be subtitute for another course. equvelent or similar GEs.
    is_optional: bool # class doesn't have to appear on final schedule.
    unit: int
