import streamlit as st
import json
import os

def load_nvim_commands():
    with open('all_commands.json', 'r') as file:
        return json.load(file)

def load_user_data(user_pseudo):
    user_file = f"{user_pseudo}.json"
    if os.path.exists(user_file):
        with open(user_file, 'r') as file:
            return json.load(file)
    else:
        return load_nvim_commands()

def save_user_data(user_pseudo, data):
    user_file = f"{user_pseudo}.json"
    with open(user_file, 'w') as file:
        json.dump(data, file)

# User account creation
user_pseudo = st.sidebar.text_input("Enter your pseudo to create an account:")
if user_pseudo:
    nvim_commands = load_user_data(user_pseudo)
else:
    nvim_commands = load_nvim_commands()

# Command selection
selected_command_value = st.sidebar.selectbox("Choose a command:", [cmd['command'] for cmd in nvim_commands])
selected_command_index = [cmd['command'] for cmd in nvim_commands].index(selected_command_value)
selected_command = nvim_commands[selected_command_index]

# Display selected command options
st.write(f"Selected Command: {selected_command['command']}")
option1 = st.button("I know it")
option2 = st.button("?")
option3 = st.button("More")

if option1:
    # Remove the command from the dictionary
    nvim_commands.pop(selected_command_index)
    # Save the updated data
    save_user_data(user_pseudo, nvim_commands)

elif option2:
    st.write(f"Explanation: {selected_command['explanation']}")

elif option3:
    st.write("Links for more information:")
    for link in selected_command['documentation_links']:
        st.write(link)

cheat_sheet_links = [
    "https://phoenixnap.com/kb/wp-content/uploads/2021/11/vim-commands-cheat-sheet-by-pnap.pdf",
    "https://link-to-another-cheat-sheet.com",
    # Add more links as needed
]

cheat_sheet_html = "<div style='background-color: #f0f0f0; padding: 20px; border-radius: 10px;'>"
cheat_sheet_html += "<h3 style='color: #333;'>Cheat Sheets:</h3><ul>"
for link in cheat_sheet_links:
    cheat_sheet_html += f"<li><a href='{link}' target='_blank' style='color: #007bff;'>{link}</a></li>"
cheat_sheet_html += "</ul></div>"

st.markdown(cheat_sheet_html, unsafe_allow_html=True)

