# Import necessary modules.
from github import Github
from ..Formatters.CodeforcesFormatter import CodeforcesFormatter
from ..Formatters.CsesFormatter import CsesFormatter
from ..Formatters.VjudgeFormatter import VjudgeFormatter

# Define a class called 'ReadMeBuilder'.
class ReadMeBuilder():
    def __init__(self, data):
        # List of supported platforms.
        self.platforms = ["Codeforces", "Cses", "Vjudge"]

        # Create a GitHub instance using the provided access token.
        git = Github(data.get("access_token"))
        self.repo = git.get_user(data.get("repo_owner")).get_repo(data.get("repo_name"))

    def get_formatter(self, name):
        # Return the appropriate formatter based on the platform name.
        if name == "Cses":
            return CsesFormatter(self.repo)
        elif name == "Codeforces":
            return CodeforcesFormatter(self.repo)
        elif name == "Vjudge":
            return VjudgeFormatter(self.repo)

    def update_readme(self, readme_content):
        readme_path = 'README.md'
        try:
            # Try to update the existing README file.
            existing_readme = self.repo.get_contents(readme_path)
            self.repo.update_file(readme_path, "Update README.md", readme_content, existing_readme.sha)
            print("README.md updated.")
        except Exception as e:
            # If the README doesn't exist, create it.
            self.repo.create_file(readme_path, "Create README.md", readme_content)
            print("README.md created.")

    def build(self):
        readme_content = "Submissions\n======================\n> *Auto-generated with ❤ using [Secpar](https://github.com/MostafaGalal1/Secpar)*\n\n## Introduction\n\nA repository to keep track of problem solving practice, containing solutions from platforms:\n\n"

        for platform in self.platforms:
            # Generate formatted content for each platform and append it to the overall readme content.
            formatted_platform_content = self.get_formatter(platform).format()
            readme_content += formatted_platform_content

        return readme_content

# End of the 'ReadMeBuilder' class definition.
