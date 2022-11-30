import sys
from services.githubAPI import GithubAPI
from services.discordAPI import DiscordAPI


if __name__ == "__main__":
    webhook = sys.argv[1]
    base_url = sys.argv[2]
    repo_owner = sys.argv[3]
    repo = sys.argv[4]
    token = sys.argv[5]
    gh = GithubAPI(base_url=base_url, repo_owner=repo_owner, repo=repo, token=token)
    message = gh.get_message()
    print(f"::set-output name=discord-message::{message}")
    discord = DiscordAPI(webhook=webhook)
    discord.post_message(message=message)