
import openai, os
openai.api_key = os.environ["OPENAI_API_KEY"]
input_text = open("scripts/input.txt", encoding="utf-8").read()
response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an AI video script generator. Output JSON only."},
        {"role": "user", "content": input_text}
    ]
)
story = response.choices[0].message.content
open("story.json","w",encoding="utf-8").write(story)
print("Story generated")
