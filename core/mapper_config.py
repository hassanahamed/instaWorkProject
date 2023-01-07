from .appConstants import *

class MemberConfig():
    """Class to handle member config data
        This is to make sure that the ui and back end are not tightly coupled.
        With this config parameter we can plug and play with other ui where the componenets mapping is provided through config.
        If no config is passed, it uses the default config which can be seen in constants file.
    """

    config = {}

    def __init__(self, config=DEFAULT_MEMBER_CONFIG):
        """Initialize the config attribute with the default member config or a custom config passed as an argument"""
        self.config = config

    def get_data(self, data):
        """
        Map the data dictionary to a new dictionary with keys specified in the config attribute.
        Strip whitespace from string values in the mapped dictionary. This is to make sure that the input from the user is striped out of whitespaces.
        """
        mapped_data = {}
        for item in self.config.keys():
            value = data.get(self.config[item])
            # Strip whitespace from string values
            mapped_data[item] = value.strip() if isinstance(value, str) else value
        return mapped_data
