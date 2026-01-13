from openai import OpenAI
import os, json, base64

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

story = json.load(open("story.json", encoding="utf-8"))
os.makedirs("images", exist_ok=True)

for i, scene in enumerate(story["scenes"], start=1):
    result = client.images.generate(
        model="gpt-image-1",
        prompt=scene["image_prompt"],
        size="1024x1024"
    )

    image_base64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    with open(f"images/scene_{i}.png", "wb") as f:
        f.write(image_bytes)

print("Images generated successfully")
