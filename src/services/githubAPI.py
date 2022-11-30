import requests
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
        return requests.get(url=url, headers=headers).json()

    def get_latest_pr(self, path="pulls"):
        page = 1
        res = self.__make_request(path=path, page=page)
        while res:
            page += 1
            new_pr = res[-1]
            res = self.__make_request(path=path, page=page)
        return new_pr