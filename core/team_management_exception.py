

class TeamManagementFacadeException(Exception):
    """Exception raised for errors in the Member creation form.

    Attributes:
        message -- Error message to be wrapped
    """

    def __init__(self, errors, message="Exception raised in facade layer"):
        self.message = ''
        for error in errors:
            self.message += error + ' field --> ' +self.get_internal_message(errors[error]) + '\n'

        super().__init__(self.message)

    def get_internal_message(self, error):
        message = ''
        for err in error:
            message += err['message']
        return message