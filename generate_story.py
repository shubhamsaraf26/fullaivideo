from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

input_text = open("scripts/input.txt", encoding="utf-8").read()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an AI video script generator. Output JSON only."},
        {"role": "user", "content": input_text}
    ]
)

story = response.choices[0].message.content

with open("story.json", "w", encoding="utf-8") as f:
    f.write(story)

print("Story generated successfully")
