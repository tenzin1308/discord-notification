from services.githubAPI import GithubAPI


if __name__ == "__main__":
    gh = GithubAPI(base_url="https://api.github.com", repo_owner="tenzin1308", repo="discord-notification", token="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")
    print(gh.get_latest_pr())
