

class DisciplineDTO:
    def __init__(self, **kwargs) -> None:
        self.component_type= kwargs['component_type']
        self.educational_mode = kwargs['educational_mode']
        self.name = kwargs['name']
        self.code = kwargs['code']
        self.students = kwargs['students']
        self.professor = kwargs['professor']
        self.lcoation = kwargs['location']
        self.total_exams = kwargs['total_exams']
        self.flexible_program = kwargs['flexible_program']
        self.online_registry = kwargs['online_registry']
        self.description = kwargs['description']
        self.long_description = kwargs['long_description']