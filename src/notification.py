import sys
from services.githubAPI import GithubAPI
from services.discordAPI import DiscordAPI


if __name__ == "__main__":
    base_url = sys.argv[1]
    repo_owner = sys.argv[2]
    repo = sys.argv[3]
    token = sys.argv[4]
    webhook = sys.argv[5]
    gh = GithubAPI(base_url=base_url, repo_owner=repo_owner, repo=repo, token=token)
    message = gh.get_message()
    print(f"message: {message}")
    discord = DiscordAPI(webhook=webhook)
    status = discord.post_message(message=message)
    print(f"status: {status}")