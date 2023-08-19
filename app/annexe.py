import random
import streamlit as st
import json

# Function to load commands
def load_commands(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Load the commands
normal_commands = load_commands("/path/to/normal_commands.json")
insert_commands = load_commands("/path/to/insert_commands.json")
visual_commands = load_commands("/path/to/visual_commands.json")

# Function to display commands
def display_commands(title, commands):
    st.subheader(title)
    for cmd in commands:
        st.text(f"Command: {cmd['command']}")
        st.text(f"Explanation: {cmd['explanation']}")
        st.text("")

# Start building the Streamlit app
st.title("Neovim Commands")

# Display Normal Mode Commands
display_commands("Normal Mode", normal_commands)

# Display Insert Mode Commands
display_commands("Insert Mode", insert_commands)

# Display Visual Mode Commands
display_commands("Visual Mode", visual_commands)

# Button to display a random command
if st.button('Show Random Command'):
    all_commands = normal_commands + insert_commands + visual_commands
    random_command = random.choice(all_commands)
    st.text(f"Random Command: {random_command['command']}")
    st.text(f"Explanation: {random_command['explanation']}")
    # TODO: Handle user input to delete or re-view the command
