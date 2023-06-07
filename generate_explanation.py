import openai
import os
import requests
import sys
import json

openai.api_key = os.environ['OPENAI_API_KEY']  # Replace with your OpenAI API key

def generate_explanation(changes):
    explanations = []

    for change in changes:
        file_name = change["filename"]
        patch = change["patch"]

        # Extract the code snippet from the change
        code_lines = []
        for line in patch.split('\n'):
            if line.startswith('+') or line.startswith('-'):
                code_lines.append(line[1:])  # Remove the '+' or '-' character
        code_snippet = '\n'.join(code_lines)

        # Generate the explanation for the code change using OpenAI ChatGPT
        prompt = f'Explain the following code change in file "{file_name}":\n\n{code_snippet}'
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
        explanations.append((file_name, code_snippet, explanation))

    return explanations

# Get the pull request information from GitHub API
pull_request_number = os.environ["PR_NUMBER"]
repository = os.environ["GITHUB_REPOSITORY"]
token = os.environ["GITHUB_TOKEN"]

# Retrieve the files changed in the pull request
pull_request_url = f"https://api.github.com/repos/{repository}/pulls/{pull_request_number}"
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"Bearer {token}",
}
response = requests.get(pull_request_url, headers=headers)
pull_request_data = response.json()

changes = pull_request_data["files"]

# Generate explanations for the code changes
explanations = generate_explanation(changes)

# Print the code snippets and their corresponding explanations
for file_name, code_snippet, explanation in explanations:
    print("File:", file_name)
    print("Code Snippet:")
    print(code_snippet)
    print("\nExplanation:")
    print(explanation)
    print()