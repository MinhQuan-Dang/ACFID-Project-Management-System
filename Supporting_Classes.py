# Base class representing a country involved in a project
class Country:
    def __init__(self, country_name, project_number, total_funding):
        # Initialize private attributes for country
        self.__country_name = country_name      # Name of the country
        self.__project_number = project_number  # Number of projects in the country
        self.__total_funding = total_funding    # Total funding for projects in the country
        self.__focus_area = []                  # List of focus areas in the country

    # String representation for a Country object
    def __str__(self):
        return self.__country_name


# Subclass for countries in the Asia region
class AsiaCountry(Country):
    def __init__(self, country_name, project_number, total_funding, region="Asia"):
        # Call the base class constructor and set the region to Asia
        super().__init__(country_name, project_number, total_funding)
        self.__region = region  # Region of the country

    def __str__(self):
        # Include region in the string representation
        return super().__str__() + f"\nRegion: {self.__region}"


# Subclass for countries in the Pacific region
class PacificCountry(Country):
    def __init__(self, country_name, project_number, total_funding, region="Pacific"):
        # Call the base class constructor and set the region to Pacific
        super().__init__(country_name, project_number, total_funding)
        self.__region = region     # Region of the country

    def __str__(self):
        # Include region in the string representation
        return super().__str__() + f"\nRegion: {self.__region}"


# Subclass for countries in the Europe region
class EuropeCountry(Country):
    def __init__(self, country_name, project_number, total_funding, region="Europe"):
        # Call the base class constructor and set the region to Europe
        super().__init__(country_name, project_number, total_funding)
        self.__region = region

    def __str__(self):
        # Include region in the string representation
        return super().__str__() + f"\nRegion: {self.__region}"


# Class to represent a focus area in a project
class FocusArea:
    def __init__(self, area_name, project_number, total_funding):
        # Initialize private attributes for focus area
        self.__area_name = area_name            # Name of the focus area
        self.__project_number = project_number  # Number of projects in this focus area
        self.__total_funding = total_funding    # Total funding for this focus area
        self.__organizations = []               # List of organizations in the focus area

    def __str__(self):
        return self.__area_name

    # Method to add an organization to the focus area
    def addOrganizations(self, organization):
        self.__organizations.append(organization)


# Class to represent an organization involved in projects
class Organization:
    def __init__(self, organization_name, total_funding):
        # Initialize private attributes for organization
        self.__organization_name = organization_name    # Name of the organization
        self.__total_funding = total_funding            # Total funding received by the organization

    def __str__(self):
        return self.__organization_name