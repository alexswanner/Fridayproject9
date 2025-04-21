import tkinter as tk
from tkinter import messagebox
import openai
from dotenv import load_dotenv
import os

# Load the .env file and get the API key
load_dotenv()

# Get the API key from environment
api_key = os.getenv("OPENAI_API_KEY")

# Check if the key was found
if not api_key:
    messagebox.showerror("Error", "API key not found. Please check your .env file.")
    print("API key not found. Exiting...")
    exit()

print(f"API Key successfully loaded: {api_key[:10]}...")  # Debug: print first 10 characters of the key

# Set up OpenAI API with the loaded key
openai.api_key = api_key

# Function to get completion from OpenAI API using the chat-based model
def get_completion():
    prompt = prompt_entry.get()  # Get the prompt from the user
    if not prompt:
        messagebox.showwarning("Input Error", "Please enter a prompt.")
        return

    try:
        # Call OpenAI API to get the completion using the chat-based model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Using the newer GPT-3.5 model
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Get the result from the API response and display it
        result = response['choices'][0]['message']['content'].strip()
        output_box.delete(1.0, tk.END)  # Clear previous output
        output_box.insert(tk.END, result)  # Insert the new result

    except Exception as e:
        messagebox.showerror("API Error", f"An error occurred: {str(e)}")

# Set up the main GUI window
root = tk.Tk()
root.title("OpenAI Prompt Completion")

# Instructions label
instructions_label = tk.Label(root, text="Enter your prompt below and click 'Submit' to get a response from OpenAI:")
instructions_label.pack(pady=10)

# Text entry for prompt
prompt_entry = tk.Entry(root, width=50)
prompt_entry.pack(pady=10)

# Submit button
submit_button = tk.Button(root, text="Submit", command=get_completion)
submit_button.pack(pady=5)

# Output box for displaying the response
output_box = tk.Text(root, height=10, width=50)
output_box.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
