import requests
from datetime import datetime
import json


class GithubAPI:
    def __init__(self, base_url, repo_owner, repo, token):
        self.__api_url = f"{base_url}/repos/{repo_owner}/{repo}"
        self.__token = token

    def __get_url(self, path, page):
        return f"{self.__api_url}/{path}?page={page}"

    def __make_request(self, path, page):
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.__token}"
        }
        url = self.__get_url(path=path, page=page)
        try:
            return requests.get(url=url, headers=headers).json()
        except Exception as e:
            print(f"Exception during API: {e}")

    def __get_latest_pr(self, path="pulls"): # TODO: add more methods for different calls
        page = 1
        res = self.__make_request(path=path, page=page)
        while res:
            page += 1
            new_pr = res[-1] if len(res) != 0 else []
            res = self.__make_request(path=path, page=page)
        return new_pr

    def get_message(self):
        pr = self.__get_latest_pr()
        # TODO: Convert the created_at (from response to local time)
        #  convert UTC to local
        #  strip the Hour and Min
        #  convert to 12 hr
        now = datetime.now()
        created_at = now.strftime("%I:%M %p")

        return {
            "author_name": pr["user"]["login"],
            "author_icon": pr["user"]["avatar_url"],
            "from_branch": pr["head"]["ref"],
            "to_branch": pr["base"]["ref"],
            "pr_link": pr["html_url"],
            "pr_title": pr["title"],
            "pr_date": created_at
        }
