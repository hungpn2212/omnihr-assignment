class EmployeeColumn:
    FIRST_NAME = 'first_name'
    LAST_NAME = 'last_name'
    EMAIL = 'email'
    PHONE_NUMBER = 'phone_number'
    DEPARTMENT = 'department'
    POSITION = 'position'
    LOCATION = 'location'
    
    @classmethod
    def get_all_columns(cls):
        return (
            cls.FIRST_NAME,
            cls.LAST_NAME,
            cls.EMAIL,
            cls.PHONE_NUMBER,
            cls.DEPARTMENT,
            cls.POSITION,
            cls.LOCATION,
        )