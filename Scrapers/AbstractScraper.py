import json
import requests
from abc import ABC, abstractmethod
from github import Github

requests.packages.urllib3.disable_warnings()


class AbstractScraper(ABC):
    def __init__(self, platform, username, password, repo_owner, repo_name, access_token):
        # todo: put in try except to check access token validity
        git = Github(access_token)

        self.platform = platform
        self.username = username
        self.password = password
        self.headers = {"accept": "application/json, text/javascript, */*; q=0.01",
                        "accept-language": "en-GB,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,en-US;q=0.6",
                        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "sec-ch-ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
                        "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "x-requested-with": "XMLHttpRequest",
                        "Referer": self.username, "Referrer-Policy": "strict-origin-when-cross-origin"}
        self.current_submissions = {}
        self.extensions = {}
        self.readme_content = None
        self.repo = git.get_user(repo_owner).get_repo(repo_name)

    def scrape(self):
        self.load_extensions()
        self.load_already_added()
        self.login()
        self.get_submissions()
        self.push_readme()

    def load_extensions(self):
        with open(f'../resources/Extensions/{self.platform}Extensions.json', 'r') as json_file:
            self.extensions = json.load(json_file)

    def load_already_added(self):
        submissions_path = f'submissions/{self.platform}Submissions.json'
        try:
            self.current_submissions = self.repo.get_contents(submissions_path).decoded_content.decode('utf-8')
        except:
            self.repo.create_file(submissions_path, "Create CodeforcesSubmissions.json", '')
            self.current_submissions = {}

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def get_submissions(self):
        pass

    @abstractmethod
    def get_submission_html(self, submission):
        pass

    def check_already_added(self, submission_id):
        if self.current_submissions[f'{submission_id}'] is not None:
            return True
        return False

    @abstractmethod
    def generate_directory_link(self, submission):
        pass

    # todo: update content of readme
    def update_readme(self):
        pass

    def push_readme(self):
        self.readme_content += '\n'
        readme_path = 'README.md'
        self.repo.update_file(readme_path, "Update README.md", self.readme_content,
                              self.repo.get_contents(readme_path).sha)
