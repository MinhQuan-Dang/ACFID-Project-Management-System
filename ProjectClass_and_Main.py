import json
import matplotlib.pyplot as plt
import Supporting_Classes
import Exception_and_Validation


# Class to represent a project with various attributes and methods
class Project:
    projects = []   # Class attribute to hold all project instances

    def __init__(self, project_name, total_funding, organization, focus_area, country,
                 project_email, project_budget, project_period):
        # Initialize private attributes for project
        self.__project_name = project_name      # Name of the project
        self.__total_funding = total_funding    # Total funding for the project
        self.__organization = organization      # Organization handling the project
        self.__focus_area = focus_area          # Focus area of the project
        self.__country = country                # Country where the project is based
        self.__project_email = project_email    # Email contact for the project
        self.__project_budget = project_budget  # Budget of the project
        self.__project_period = project_period  # Duration of the project

    def __str__(self):
        # Return a formatted string with project details
        return (f"Project Name: {self.__project_name}\n"
                f"Total Funding: {self.__total_funding}\n"
                f"Organization: {self.__organization}\n"
                f"Focus Area: {self.__focus_area}\n"
                f"Base Country: {self.__country}\n"
                f"Project Email: {self.__project_email}\n"
                f"Project Budget: {self.__project_budget}\n"
                f"Project Period: {self.__project_period}\n")

    # Getter methods to access private attributes
    def getProjectName(self):
        return self.__project_name

    def getFunding(self):
        return self.__total_funding

    def getOrganization(self):
        return self.__organization

    def getFocusArea(self):
        return self.__focus_area

    def getCountry(self):
        return self.__country

    def getProjectEmail(self):
        return self.__project_email

    def getProjectBudget(self):
        return self.__project_budget

    def getProjectPeriod(self):
        return self.__project_period

    # Setter methods to modify private attributes
    def setFunding(self, total_funding):
        self.__total_funding = total_funding

    def setOrganization(self, organization):
        self.__organization = organization

    def setFocusArea(self, focus_area):
        self.__focus_area = focus_area

    def setCountry(self, country):
        self.__country = country

    def setProjectEmail(self, email):
        self.__project_email = email

    def setProjectBudget(self, budget):
        self.__project_budget = budget

    def setProjectPeriod(self, period):
        self.__project_period = period

    @staticmethod
    def search_by_name(name):
        # Search for a project by name in the list of projects
        for p in Project.projects:
            if p.getProjectName() == name:
                return p
        return None

    # Convert project attributes to a dictionary for serialization
    def to_dict(self):
        return {
            'project_name': self.__project_name,
            'total_funding': self.__total_funding,
            'organization': self.__organization,
            'focus_area': self.__focus_area,
            'base_country': self.__country, 
            'project_email': self.__project_email,
            'project_budget': self.__project_budget,
            'project_period': self.__project_period
        }


    @staticmethod
    def from_dict(data):
        # Create a Project instance from a dictionary, handling missing keys
        normalized_data = {key.lower().replace(' ', '_'): value for key, value in data.items()}
        return Project(
            normalized_data.get('project_name', 'Unnamed Project'),
            normalized_data.get('total_funding', 0.0),
            normalized_data.get('organization', 'Unknown Organization'),
            normalized_data.get('focus_area', 'Unknown Focus Area'),
            normalized_data.get('base_country', 'Unknown Country'),
            normalized_data.get('project_email', 'noemail@example.com'),
            normalized_data.get('project_budget', '$0.00'),
            normalized_data.get('project_period', 'Unknown Period')
        )


    @staticmethod
    def load_projects_from_json(filename):
        # Load projects from a JSON file and add them to the list of projects
        try:
            with open(filename, 'r') as file:
                data_list = json.load(file)
                for idx, data in enumerate(data_list):
                    try:
                        project = Project.from_dict(data)
                        Project.projects.append(project)
                    except KeyError as e:
                        print(f"Missing key {e} in project at index {idx}. Please check your JSON file.")
            print(f"Projects have been successfully loaded from {filename}")
            # Automatically print all projects after loading
            for project in Project.projects:
                print(project)
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def write_projects_to_json(filename):
        # Write projects to a JSON file
        data_list = [project.to_dict() for project in Project.projects]
        try:
            with open(filename, 'w') as file:
                json.dump(data_list, file, indent=4)
            print(f"Projects have been successfully written to {filename}")
        except IOError as e:
            print(f"An I/O error occurred: {e}")

    @staticmethod
    def load_projects_from_file(filename):
        # Load projects from a text file and add them to the list of projects
        try:
            with open(filename, 'r') as file:
                project_data = {}
                line_number = 0
                for line in file:
                    line_number += 1
                    line = line.strip()
                    if line:
                        # Process valid lines with key-value pairs
                        if ': ' in line:
                            key, value = line.split(': ', 1)
                            project_data[key.strip()] = value.strip()
                        else:
                            print(f"Skipping invalid line {line_number}: '{line}'")
                    else:
                        # Create and add project when an empty line is encountered
                        if project_data:
                            project = Project(
                                project_data.get('Project Name'),
                                project_data.get('Total Funding'),
                                project_data.get('Organization'),
                                project_data.get('Focus Area'),
                                project_data.get('Base Country'),
                                project_data.get('Project Email'),
                                project_data.get('Project Budget'),
                                project_data.get('Project Period')
                            )
                            Project.projects.append(project)
                            project_data = {}
                # Add the last project if file doesn't end with an empty line
                if project_data:
                    project = Project(
                        project_data.get('Project Name'),
                        project_data.get('Total Funding'),
                        project_data.get('Organization'),
                        project_data.get('Focus Area'),
                        project_data.get('Base Country'),
                        project_data.get('Project Email'),
                        project_data.get('Project Budget'),
                        project_data.get('Project Period')
                    )
                    Project.projects.append(project)
            print(f"Projects have been successfully loaded from {filename}")
            # Automatically print all projects after loading
            for project in Project.projects:
                print(project)
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def write_projects_to_file(filename):
        # Write projects to a text file
        try:
            with open(filename, 'w') as file:
                for project in Project.projects:
                    file.write(str(project))
                    file.write("\n")
            print(f"Projects have been successfully written to {filename}")
        except IOError as e:
            print(f"An I/O error occurred: {e}")


# Main block for interactive console application
if __name__ == "__main__":
    while True:
        # Display menu options to the user
        print("\nPlease enter your choice:")
        print("I or i to import text files")
        print("J or j to import json files")
        print("C or c to create projects")
        print("M or m to modify projects")
        print("G or g to generate summary report and charts for country or organization")
        print("E or e to export json files")
        print("F or f to generate figures for all projects")
        print("X or x to exit")
        choice = input("Your choice: ").strip()

        try:
            # Validate user choice
            InvalidChoiceException.validate_choice(choice)
        except InvalidChoiceException as e:
            print(e)
            continue

        if choice.upper() == 'X':
            # Exit option: Save projects to file before exiting
            txt_filename = input("Enter the filename to save projects to (e.g., 'ACFID_projects_updated.txt'): ").strip()
            json_filename = input("Enter the JSON filename to save projects to (e.g., 'ACFID_projects_updated.json'): ").strip()
            Project.write_projects_to_file(txt_filename)
            Project.write_projects_to_json(json_filename)
            print(f"Projects saved to '{txt_filename}' and '{json_filename}'.")
            break

        elif choice.upper() == 'I':
            # Import projects from text file
            file_name = input("Please enter the text file name to import: ")
            Project.load_projects_from_file(file_name)

        elif choice.upper() == 'J':
            # Import projects from JSON file
            file_name = input("Please enter the JSON file name to import: ")
            Project.load_projects_from_json(file_name)

        elif choice.upper() == 'E':
            # Export projects to JSON file
            file_name = input("Please enter the JSON file name to export to: ")
            Project.write_projects_to_json(file_name)

        elif choice.upper() == 'F':
            # Generate figures for all projects
            if not Project.projects:
                print("No projects available to generate figures.")
                continue

            # Collect data for generating charts
            project_names = []
            budgets = []
            start_dates = []
            durations = []
            for p in Project.projects:
                budget = Validator.parse_budget(p.getProjectBudget())
                if budget == 0.0:
                    continue  # Skip projects with invalid budget
                project_names.append(p.getProjectName())
                budgets.append(budget)
                period = p.getProjectPeriod()
                start_date, end_date, duration = Validator.parse_project_period(period)
                if start_date is None:
                    continue  # Skip if period is invalid
                start_dates.append(start_date)
                durations.append(duration)

            if not project_names:
                print("No valid budget data available for generating charts.")
                continue

            # Sorting data for line chart
            sorted_indices = sorted(range(len(start_dates)), key=lambda k: start_dates[k])
            sorted_dates = [start_dates[i] for i in sorted_indices]
            sorted_budgets = [budgets[i] for i in sorted_indices]

            # Create a figure with 2x2 subplots
            fig, axs = plt.subplots(2, 2, figsize=(15, 10))

            # Budget Bar Chart
            axs[0, 0].bar(project_names, budgets)
            axs[0, 0].set_xlabel('Project Name')
            axs[0, 0].set_ylabel('Budget')
            axs[0, 0].set_title('Budget Bar Chart')
            axs[0, 0].tick_params(axis='x', rotation=45)

            # Budget Pie Chart
            axs[0, 1].pie(budgets, labels=project_names, autopct='%1.1f%%')
            axs[0, 1].set_title('Budget Pie Chart')

            # Budget Line Chart
            axs[1, 0].plot(sorted_dates, sorted_budgets, marker='o')
            axs[1, 0].set_xlabel('Project Start Date')
            axs[1, 0].set_ylabel('Budget')
            axs[1, 0].set_title('Budget Line Chart')
            axs[1, 0].tick_params(axis='x', rotation=45)

            # Budget Bubble Chart
            scatter = axs[1, 1].scatter(durations, budgets, s=[b/1000 for b in budgets], alpha=0.5)
            axs[1, 1].set_xlabel('Project Duration (Days)')
            axs[1, 1].set_ylabel('Budget')
            axs[1, 1].set_title('Budget Bubble Chart')

            plt.tight_layout()
            plt.savefig('Combined_Budget_Charts_All_Projects.png')
            plt.show()

            print("Combined figure generated and saved as 'Combined_Budget_Charts_All_Projects.png'.")

        elif choice.upper() == 'C':
            # Code for creating a new project
            project_name = input("Please enter the new project name: ")

            while True:
                try:
                    project_funding = float(input("Please enter the total funding: "))
                    break
                except ValueError:
                    print("Invalid Input. Please enter a valid float number for total funding.")

            while True:
                try:
                    project_org = input("Please enter the organization name: ")
                    InvalidOrganizationException.validate_organization(project_org)
                    break
                except InvalidOrganizationException as e:
                    print(e)

            while True:
                try:
                    project_fa = input("Please enter the focus area: ")
                    InvalidFocusAreaException.validate_focus_area(project_fa)
                    break
                except InvalidFocusAreaException as e:
                    print(e)

            while True:
                try:
                    project_country = input("Please enter the country name: ")
                    InvalidCountryException.validate_country(project_country)
                    break
                except InvalidCountryException as e:
                    print(e)

            while True:
                project_email = input("Please enter the project email: ")
                if Validator.validate_email(project_email):
                    break
                else:
                    print("Invalid email format. Please enter a valid email address.")

            while True:
                project_budget = input("Please enter the project budget (e.g., $12,345.67): ")
                if Validator.validate_budget(project_budget):
                    break
                else:
                    print("Invalid budget format. Please enter a valid budget.")

            while True:
                project_period = input("Please enter the project period (DD/MM/YYYY ~ DD/MM/YYYY): ")
                if Validator.validate_project_period(project_period):
                    break
                else:
                    print("Invalid project period format. Please enter in 'DD/MM/YYYY ~ DD/MM/YYYY' format.")

            new_project = Project(
                project_name,
                project_funding,
                project_org,
                project_fa,
                project_country,
                project_email,
                project_budget,
                project_period
            )
            Project.projects.append(new_project)
            print("Project added successfully.")

        elif choice.upper() == 'M':
            project_name = input("Please enter the project name that you want to modify: ")
            project = Project.search_by_name(project_name)
            if project is None:
                print("Project not found.")
            else:
                # Modify total funding
                while True:
                    funding_input = input(f"Please enter the total funding (current: {project.getFunding()}) (press Enter to keep current value): ")
                    if funding_input == '':
                        break  # Keep current value
                    else:
                        try:
                            project_funding = float(funding_input)
                            project.setFunding(project_funding)
                            break
                        except ValueError:
                            print("Invalid Input. Please enter a valid float number for total funding.")

                # Modify organization
                while True:
                    project_org = input(f"Please enter the organization name (current: {project.getOrganization()}) (press Enter to keep current value): ")
                    if project_org == '':
                        break  # Keep current value
                    else:
                        try:
                            InvalidOrganizationException.validate_organization(project_org)
                            project.setOrganization(project_org)
                            break
                        except InvalidOrganizationException as e:
                            print(e)

                # Modify focus area
                while True:
                    project_fa = input(f"Please enter the focus area (current: {project.getFocusArea()}) (press Enter to keep current value): ")
                    if project_fa == '':
                        break  # Keep current value
                    else:
                        try:
                            InvalidFocusAreaException.validate_focus_area(project_fa)
                            project.setFocusArea(project_fa)
                            break
                        except InvalidFocusAreaException as e:
                            print(e)

                # Modify country
                while True:
                    project_country = input(f"Please enter the country name (current: {project.getCountry()}) (press Enter to keep current value): ")
                    if project_country == '':
                        break  # Keep current value
                    else:
                        try:
                            InvalidCountryException.validate_country(project_country)
                            project.setCountry(project_country)
                            break
                        except InvalidCountryException as e:
                            print(e)

                # Modify project email
                while True:
                    project_email = input(f"Please enter the project email (current: {project.getProjectEmail()}) (press Enter to keep current value): ")
                    if project_email == '':
                        break  # Keep current value
                    else:
                        if Validator.validate_email(project_email):
                            project.setProjectEmail(project_email)
                            break
                        else:
                            print("Invalid email format. Please enter a valid email address.")

                # Modify project budget
                while True:
                    project_budget = input(f"Please enter the project budget (current: {project.getProjectBudget()}) (press Enter to keep current value): ")
                    if project_budget == '':
                        break  # Keep current value
                    else:
                        if Validator.validate_budget(project_budget):
                            project.setProjectBudget(project_budget)
                            break
                        else:
                            print("Invalid budget format. Please enter a valid budget.")

                # Modify project period
                while True:
                    project_period = input(f"Please enter the project period (current: {project.getProjectPeriod()}) (press Enter to keep current value): ")
                    if project_period == '':
                        break  # Keep current value
                    else:
                        if Validator.validate_project_period(project_period):
                            project.setProjectPeriod(project_period)
                            break
                        else:
                            print("Invalid project period format. Please enter in 'DD/MM/YYYY ~ DD/MM/YYYY' format.")

                print("Project updated successfully.")

        elif choice.upper() == 'G':
            summary_type = input("Do you want to generate report for country (C or c) or organization (O or o): ")
            if summary_type.upper() == 'C':
                country_name = input("Please enter the country name: ")
                country_summary = [p for p in Project.projects if p.getCountry() == country_name]
                if not country_summary:
                    print("No projects found for the specified country.")
                else:
                    filename = f"ACFID_report_{country_name}.txt"
                    try:
                        with open(filename, 'w') as file:
                            file.write(f"There are {len(country_summary)} projects in {country_name}\n")
                            for project in country_summary:
                                file.write(str(project))
                                file.write("\n")
                        print(f"Projects have been successfully written to {filename}")
                    except IOError as e:
                        print(f"An I/O error occurred: {e}")

                    # Generate figures using matplotlib
                    project_names = []
                    budgets = []
                    start_dates = []
                    durations = []
                    for p in country_summary:
                        budget = Validator.parse_budget(p.getProjectBudget())
                        if budget == 0.0:
                            continue  # Skip projects with invalid budget
                        project_names.append(p.getProjectName())
                        budgets.append(budget)
                        period = p.getProjectPeriod()
                        start_date, end_date, duration = Validator.parse_project_period(period)
                        if start_date is None:
                            continue  # Skip if period is invalid
                        start_dates.append(start_date)
                        durations.append(duration)

                    if not project_names:
                        print("No valid budget data available for generating charts.")
                        continue

                    # Sorting data for line chart
                    sorted_indices = sorted(range(len(start_dates)), key=lambda k: start_dates[k])
                    sorted_dates = [start_dates[i] for i in sorted_indices]
                    sorted_budgets = [budgets[i] for i in sorted_indices]

                    # Create a figure with 2x2 subplots
                    fig, axs = plt.subplots(2, 2, figsize=(15, 10))

                    # Budget Bar Chart
                    axs[0, 0].bar(project_names, budgets)
                    axs[0, 0].set_xlabel('Project Name')
                    axs[0, 0].set_ylabel('Budget')
                    axs[0, 0].set_title(f'Budget Bar Chart for Projects in {country_name}')
                    axs[0, 0].tick_params(axis='x', rotation=45)

                    # Budget Pie Chart
                    axs[0, 1].pie(budgets, labels=project_names, autopct='%1.1f%%')
                    axs[0, 1].set_title(f'Budget Pie Chart for Projects in {country_name}')

                    # Budget Line Chart
                    axs[1, 0].plot(sorted_dates, sorted_budgets, marker='o')
                    axs[1, 0].set_xlabel('Project Start Date')
                    axs[1, 0].set_ylabel('Budget')
                    axs[1, 0].set_title(f'Budget Line Chart Over Time for {country_name}')
                    axs[1, 0].tick_params(axis='x', rotation=45)

                    # Budget Bubble Chart
                    scatter = axs[1, 1].scatter(durations, budgets, s=[b/1000 for b in budgets], alpha=0.5)
                    axs[1, 1].set_xlabel('Project Duration (Days)')
                    axs[1, 1].set_ylabel('Budget')
                    axs[1, 1].set_title(f'Budget Bubble Chart for Projects in {country_name}')

                    plt.tight_layout()
                    plt.savefig(f'Combined_Budget_Charts_{country_name}.png')
                    plt.show()

            elif summary_type.upper() == 'O':
                organization_name = input("Please enter the organization name: ")
                org_summary = [p for p in Project.projects if p.getOrganization() == organization_name]
                if not org_summary:
                    print("No projects found for the specified organization.")
                else:
                    filename = f"ACFID_report_{organization_name}.txt"
                    try:
                        with open(filename, 'w') as file:
                            file.write(f"There are {len(org_summary)} projects in {organization_name}\n")
                            for project in org_summary:
                                file.write(str(project))
                                file.write("\n")
                        print(f"Projects have been successfully written to {filename}")
                    except IOError as e:
                        print(f"An I/O error occurred: {e}")

                    # Generate figures using matplotlib
                    project_names = []
                    budgets = []
                    start_dates = []
                    durations = []
                    for p in org_summary:
                        budget = Validator.parse_budget(p.getProjectBudget())
                        if budget == 0.0:
                            continue  # Skip projects with invalid budget
                        project_names.append(p.getProjectName())
                        budgets.append(budget)
                        period = p.getProjectPeriod()
                        start_date, end_date, duration = Validator.parse_project_period(period)
                        if start_date is None:
                            continue  # Skip if period is invalid
                        start_dates.append(start_date)
                        durations.append(duration)

                    if not project_names:
                        print("No valid budget data available for generating charts.")
                        continue

                    # Sorting data for line chart
                    sorted_indices = sorted(range(len(start_dates)), key=lambda k: start_dates[k])
                    sorted_dates = [start_dates[i] for i in sorted_indices]
                    sorted_budgets = [budgets[i] for i in sorted_indices]

                    # Create a figure with 2x2 subplots
                    fig, axs = plt.subplots(2, 2, figsize=(15, 10))

                    # Budget Bar Chart
                    axs[0, 0].bar(project_names, budgets)
                    axs[0, 0].set_xlabel('Project Name')
                    axs[0, 0].set_ylabel('Budget')
                    axs[0, 0].set_title(f'Budget Bar Chart for Projects by {organization_name}')
                    axs[0, 0].tick_params(axis='x', rotation=45)

                    # Budget Pie Chart
                    axs[0, 1].pie(budgets, labels=project_names, autopct='%1.1f%%')
                    axs[0, 1].set_title(f'Budget Pie Chart for Projects by {organization_name}')

                    # Budget Line Chart
                    axs[1, 0].plot(sorted_dates, sorted_budgets, marker='o')
                    axs[1, 0].set_xlabel('Project Start Date')
                    axs[1, 0].set_ylabel('Budget')
                    axs[1, 0].set_title(f'Budget Line Chart Over Time for {organization_name}')
                    axs[1, 0].tick_params(axis='x', rotation=45)

                    # Budget Bubble Chart
                    scatter = axs[1, 1].scatter(durations, budgets, s=[b/1000 for b in budgets], alpha=0.5)
                    axs[1, 1].set_xlabel('Project Duration (Days)')
                    axs[1, 1].set_ylabel('Budget')
                    axs[1, 1].set_title(f'Budget Bubble Chart for Projects by {organization_name}')

                    plt.tight_layout()
                    plt.savefig(f'Combined_Budget_Charts_{organization_name}.png')
                    plt.show()
            else:
                print("Invalid choice.")

        else:
            print("Invalid choice. Please try again.")