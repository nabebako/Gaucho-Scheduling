from .class_time_location import Class_Time_Location

class Section_Info:
    enroll_code: str
    section: str
    session: str
    classClosed: str
    enrolled_total: int
    max_enroll: int
    secondary_status: str
    is_department_approval_required: bool
    is_instructor_approval_required: bool
    concurrent_courses: [str]
    time_and_location: [Class_Time_Location]
    instructor: [str]
