class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self, name="", typing="", reflection=True, year=None):
        self.name = name
        self.typing = typing.title()
        self.reflection = reflection
        self.year = year
