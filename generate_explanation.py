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
token = os.environ["GITHUB_TOKEN"]

pull_request_url = f"https://api.github.com/repos/{repository}/pulls/{pull_request_number}"
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"Bearer {token}",
}

response = requests.get(pull_request_url, headers=headers)
pull_request_data = response.json()

# Extract the code changes from the pull request
changes = pull_request_data["body"]  # Assuming the changes are in the pull request body

# Generate explanation using ChatGPT
explanation = generate_explanation(changes)

# Print or use the generated explanation as needed
print(explanation)
