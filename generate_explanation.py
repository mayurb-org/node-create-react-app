import os
import openai

def generate_explanation(changes):
    # Authenticate with OpenAI
    openai.api_key = os.environ['OPENAI_API_KEY']

    # Generate explanation using the ChatGPT API
    explanation = openai.Completion.create(
        engine='text-davinci-003',
        prompt=changes,
        max_tokens=256,
        n=1,
        stop=None
    ).choices[0].text.strip()

    return explanation

# Usage: generate_explanation(changes)
# Replace 'changes' with the relevant changes or description of the pull request

changes = ...
explanation = generate_explanation(changes)

print(explanation)
