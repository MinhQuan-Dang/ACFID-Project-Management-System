import re
from datetime import datetime

# Exception class for handling invalid choices in user input
class InvalidChoiceException(Exception):
    @staticmethod
    def validate_choice(choice):
        # List of valid choices for the menu
        valid_choices = ['I', 'i', 'J', 'j', 'C', 'c', 'M', 'm', 'G', 'g', 'E', 'e', 'F', 'f', 'X', 'x']
        if choice not in valid_choices:
            raise InvalidChoiceException(f"Invalid choice: {choice}")


# Exception class for handling invalid countries
class InvalidCountryException(Exception):
    # List of valid countries
    valid_countries = ["United States", "Canada", "Mexico", "Brazil", "Argentina", "United Kingdom",
                       "France", "Germany", "Italy", "Spain", "Australia", "New Zealand", "China",
                       "India", "Japan", "Fiji", "Nepal", "Ukraine", "Romania"] 

    @staticmethod
    def validate_country(country):
        if country not in InvalidCountryException.valid_countries:
            raise InvalidCountryException(f"Invalid country: {country}")


# Exception class for handling invalid organizations
class InvalidOrganizationException(Exception):
    # List of valid organizations
    valid_organizations = ["Oxfam Australia", "World Vision Australia", "CARE Australia", "Save the Children Australia",
                           "Plan International Australia", "Caritas Australia", "The Fred Hollows Foundation",
                           "Australian Red Cross", "ActionAid Australia", "Islamic Relief Australia",
                           "Good Neighbours Australia", "ChildFund Australia", "TEAR Australia",
                           "Union Aid Abroad-APHEDA", "Habitat for Humanity Australia",
                           "International Women's Development Agency", "Australian Volunteers International",
                           "Engineers Without Borders Australia", "UOW", "AVI", "Anglican Relief and Development Fund Australia",
                           "Act for Peace", "International Justice Mission Australia", "Org A", "Org B"] 

    @staticmethod
    def validate_organization(organization):
        if organization not in InvalidOrganizationException.valid_organizations:
            raise InvalidOrganizationException(f"Invalid organization: {organization}")


# Exception class for handling invalid focus areas
class InvalidFocusAreaException(Exception):
    # List of valid focus areas
    valid_focus_areas = ["Humanitarian Action", "Sustainable Development", "Climate Change", "Gender Equality",
                         "Inclusive and Locally Led Development", "Civil Society Strengthening",
                         "Governance and Accountability", "Health and Education", "Agriculture",
                         "Child Focused", "Health", "Emergency & Humanitarian Aid",
                         "Conflict prevention, peace and security"] 

    @staticmethod
    def validate_focus_area(area):
        if area not in InvalidFocusAreaException.valid_focus_areas:
            raise InvalidFocusAreaException(f"Invalid focus area: {area}")


# Validator class for various input validations
class Validator:
    @staticmethod
    def validate_email(email):
        # Regex pattern for email validation
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    @staticmethod
    def validate_budget(budget):
        # Regex pattern for budget validation
        pattern = r'^\$?\d+(,\d{3})*(\.\d{2})?$'
        return re.match(pattern, budget) is not None

    @staticmethod
    def parse_budget(budget_str):
        # Remove '$' and ',' and convert to float
        budget_str = budget_str.replace('$', '').replace(',', '')
        try:
            budget = float(budget_str)
            return budget
        except ValueError:
            return 0.0  # Return 0.0 for invalid budgets

    @staticmethod
    def validate_project_period(period):
        # Regex pattern for project period validation
        # Expected format: 'DD/MM/YYYY ~ DD/MM/YYYY'
        pattern = r'^\d{2}/\d{2}/\d{4}\s*~\s*\d{2}/\d{2}/\d{4}$'
        return re.match(pattern, period) is not None

    @staticmethod
    def parse_project_period(period_str):
        # Parse project period string into start and end dates, and calculate duration
        # Expected format: 'DD/MM/YYYY ~ DD/MM/YYYY'
        try:
            start_str, end_str = period_str.split('~')
            start_str = start_str.strip()
            end_str = end_str.strip()
            start_date = datetime.strptime(start_str, '%d/%m/%Y')
            end_date = datetime.strptime(end_str, '%d/%m/%Y')
            duration = (end_date - start_date).days
            return start_date, end_date, duration
        except Exception as e:
            return None, None, None