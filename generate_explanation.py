import os
import sys
import openai
import requests

def fetch_pull_request_diff(diff_url):
    # Fetch the pull request diff using the provided URL
    response = requests.get(diff_url)
    response.raise_for_status()
    return response.text

def generate_explanation(diff):
    # Authenticate with OpenAI
    openai.api_key = os.environ['OPENAI_API_KEY']

    # Preprocess the diff if needed
    # (e.g., extract relevant lines, remove noise, format as desired)

    # Generate explanation using the ChatGPT API
    explanation = openai.Completion.create(
        engine='text-davinci-002',
        prompt=diff,
        max_tokens=256,
        n=1,
        stop=None
    ).choices[0].text.strip()

    return explanation

if __name__ == '__main__':
    # Usage: python generate_explanation.py <pull_request_diff_url>
    # Example: python generate_explanation.py https://github.com/user/repo/pull/123.diff
    diff_url = sys.argv[1]
    diff = fetch_pull_request_diff(diff_url)
    explanation = generate_explanation(diff)

    # Print the explanation to be captured as the output in the workflow
    print(explanation)