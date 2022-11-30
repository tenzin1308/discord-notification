# discord-notification

This action sends notification to Discord when new Pull Request is created

## Inputs

### discord-webhook-url
**Required** The URL for the Discord Webhook.
### github-base-url
**Optional** The default url is for personal github,\
If you are on enterprise github account, then it is required. \
Default `"https://api.github.com"`.
### github-repo-owner
**Optional** The owner of the repo where the action is being run. \
Default `${{ github.repository_name }}`.
### github-repo-name
**Optional** The repository where where the action is being run. \
Default `${{ github.repository_name }}`.
### github-token
**Optional** Personal Access Token (PAT) created by github which is valid only during the action run time. \
Default `${{ github.token }}`.

## Outputs

### discord-message
The sample message that was posted in the discord.

## Example usage
```
jobs:
  # The workflow job name
  discord-notifier:
    # Name of the enviroment
    enviroment: secrets
    # The type of runner that the job will run on
    runs-on: ubuntu-latest
    # Sequence of tasks
    steps:
      - name: Discord Notification
        uses: tenzin1308/discord-notification@v1.0.0
        with:
          discord-webhook-url: ${{ secrets.WEBHOOKS_URL }}
```
