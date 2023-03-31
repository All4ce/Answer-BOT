from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')

def chatgpt_response(prompt):
    try:
        response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.9,
                max_tokens=1024,
                top_p = 1,
                stop=None,
                frequency_penalty=0,
                presence_penalty=0.6,
                timeout=10
        )
        response_dict = response.get("choices")
        if response_dict and len(response_dict) > 0:
            prompt_response = response_dict[0]["text"]
    except openai.error.TimeoutError:
        prompt_response = "Desculpe, o tempo limite foi atingido. Tente novamente."
        print(prompt_response)
    return prompt_response
