import os
import sys
import openai
import requests

openai.api_key = "YOUR_API_KEY"  # Replace with your OpenAI API key

def generate_explanation(changes):
    prompt = f"Changes: {changes}\n\nExplain the changes:"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=30,
    )

    explanation = response.choices[0].text.strip()
    return explanation

# Get the pull request information from GitHub API
pull_request_number = os.environ["PR_NUMBER"]
repository = os.environ["GITHUB_REPOSITORY"]
token = os.environ["GH_TOKEN"]

pull_request_url = f"https://api.github.com/repos/{repository}/pulls/{pull_request_number}"
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"Bearer {token}",
}

response = requests.get(pull_request_url, headers=headers)
pull_request_data = response.json()

To extract the code changes from a pull request, you can use the GitHub API to fetch the pull request diff. Here's an example of how you can modify the code to extract the code changes:

python

import openai
import os
import requests

openai.api_key = "YOUR_API_KEY"  # Replace with your OpenAI API key

def generate_explanation(changes):
    prompt = f"Changes: {changes}\n\nExplain the changes:"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=30,
    )

    explanation = response.choices[0].text.strip()
    return explanation

# Get the pull request information from GitHub API
pull_request_number = os.environ["PR_NUMBER"]
repository = os.environ["GITHUB_REPOSITORY"]
token = os.environ["GITHUB_TOKEN"]

pull_request_url = f"https://api.github.com/repos/{repository}/pulls/{pull_request_number}"
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"Bearer {token}",
}

response = requests.get(pull_request_url, headers=headers)
pull_request_data = response.json()

# Extract the code changes from the pull request diff
diff_url = pull_request_data["diff_url"]
response = requests.get(diff_url, headers=headers)
diff_content = response.text

# Parse the code changes from the diff content
changes = ""
lines = diff_content.split("\n")
for line in lines:
    if line.startswith("+") or line.startswith("-"):
        changes += line + "\n"

# Generate explanation using ChatGPT
explanation = generate_explanation(changes)

# Print or use the generated explanation as needed
print(explanation)
