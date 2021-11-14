class Validation:

    @staticmethod
    def decorator_string(func):
        def validate_string(self, value):
            if any(map(str.isdigit, value)):
                raise ValueError("No integers in word!")
            return func(self, value)

        return validate_string

    @staticmethod
    def decorator_filename(func):
        def validate_filename(self, value):
            if not value.endswith(".txt"):
                raise ValueError("Incorrect filename, should end with .txt")
            return func(self, value)

        return validate_filename
