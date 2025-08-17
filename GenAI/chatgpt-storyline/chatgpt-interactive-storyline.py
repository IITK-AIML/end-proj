import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# Get the OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("OPENAI_API_KEY not set in environment variables. Please set it in a .env file or your environment.")

def chatgpt_response(prompt, model="gpt-3.5-turbo"):
    client = openai.OpenAI(api_key=openai.api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def get_input(prompt):
    return input(prompt)

def main():
    print("Welcome to the Interactive ChatGPT Storytelling Adventure!")
    theme = get_input("Choose a story theme (fantasy, sci-fi, mystery, adventure): ")
    char1 = get_input("Enter the name of the first main character: ")
    char1_desc = get_input(f"Describe {char1}'s personality and background: ")
    char2 = get_input("Enter the name of the second main character: ")
    char2_desc = get_input(f"Describe {char2}'s personality and background: ")
    scene = get_input("Set the opening scene: ")

    story = f"Theme: {theme}\nCharacters: {char1} - {char1_desc}; {char2} - {char2_desc}\nScene: {scene}\n"
    print("\n--- Story Begins ---\n")
    print(story)

    current_story = story
    for i in range(3):
        user_action = get_input("What do the characters do next? ")
        prompt = f"{current_story}\nAction: {user_action}\nContinue the story, include a decision point for the user."
        ai_response = chatgpt_response(prompt)
        print(f"\nAI: {ai_response}\n")
        current_story += f"\nAction: {user_action}\n{ai_response}\n"

    print("\n--- Story End ---\n")
    print(current_story)

    # Save the story to a sharable script file
    output_path = "story.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(current_story)
    print(f"\nThe complete story has been saved to {output_path}. You can share this file!")

if __name__ == "__main__":
    main()
