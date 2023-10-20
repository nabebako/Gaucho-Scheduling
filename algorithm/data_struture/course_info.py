from .class_time_location import Class_Time_Location
from .general_education import General_Education
from .section_info import Section_Info

class Course_Info:
    course_id: str
    course_name: str
    description: str
    college: str

    subject_area: str
    unit: int
    grading_option: str
    instruction_type: str
    general_edu: [General_Education]

    lecture: [Class_Time_Location]
    
    is_close: bool
    is_cancel: bool
    grading_option: str

    level_restriction: str
    major_restriction: str
    major_restriction_pass: str
    minor_restriction: str
    minor_restriction_pass: str

    section: [Section_Info]
