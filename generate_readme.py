import json
import random
import datetime
from mood_engine import get_mood

USERNAME = "leeeshart"  # change to your GitHub username

def load_messages(mood):
    with open("data/messages.json") as f:
        data = json.load(f)
    return random.choice(data.get(mood, data["offline"]))

def load_template(mood):
    with open(f"templates/{mood}.md") as f:
        return f.read()

def generate():
    mood = get_mood(USERNAME)
    message = load_messages(mood)
    time_str = datetime.datetime.now().strftime("%H:%M_UTC")
    
    # Your static intro — edit this however you want
    intro = f"""# Hey, I'm Leesha 👋

BCA student · AI Safety & Adversarial NLP Research  
Building [SneakyLLM](https://github.com/leeeshart/SneakyLLM) · [Prompt-Safety-Classifier](https://github.com/leeeshart/Prompt-Safety-Classifier)

---

"""
    mood_section = load_template(mood)
    mood_section = mood_section.replace("{{message}}", message)
    mood_section = mood_section.replace("{{time}}", time_str)
    
    final = intro + mood_section
    
    with open("README.md", "w") as f:
        f.write(final)
    
    print(f"README updated — mood: {mood}")

if __name__ == "__main__":
    generate()
