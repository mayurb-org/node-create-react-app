import openai
import os
import requests
import sys

openai.api_key = os.environ['OPENAI_API_KEY']  # Replace with your OpenAI API key

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

# Retrieve the base and head commits
base_commit = pull_request_data["base"]["sha"]
head_commit = pull_request_data["head"]["sha"]

# Compare the base and head commits to get the code changes
compare_url = f"https://api.github.com/repos/{repository}/compare/{base_commit}...{head_commit}"
response = requests.get(compare_url, headers=headers)
compare_data = response.json()

# Extract the code changes from the compare data
changes = compare_data["files"]

# Generate explanation using ChatGPT
explanation = generate_explanation(changes)

# Print or use the generated explanation as needed
print(explanation)
