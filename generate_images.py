
import json, openai, os, base64
openai.api_key = os.environ["OPENAI_API_KEY"]
story = json.load(open("story.json"))
os.makedirs("images",exist_ok=True)
for i,scene in enumerate(story["scenes"],start=1):
    result = openai.Image.create(prompt=scene["image_prompt"],size="1024x1024")
    image_base64 = result["data"][0]["b64_json"]
    open(f"images/scene_{i}.png","wb").write(base64.b64decode(image_base64))
print("Images generated")
