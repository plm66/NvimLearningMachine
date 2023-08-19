import os
import subprocess
import sys
subprocess.run(['zsh', 'mt/init.sh'])

# d'abord je veux verifier la presence du ficher qui va permettre l'update de conda..
file_path = 'mt/venv_export.yml'

if os.path.exists(file_path):
    # File exists, do something
    print("File exists!  Philippe, keep on that way!----------")
else:
    # File does not exist
    print("File does not exist.")

# maintenant je veux quoi?
# connaître le nom de l'environnement que je vais devoir activer et dont le nom est sur le fichier venv_export.yml

try:
    with open(file_path, 'r') as file:
        content = file.read()
        environment_name = None

        # Parse the content to find the environment name
        # Assuming the environment name is stored as a key-value pair in the YAML file
        for line in content.split('\n'):
            if line.startswith('name:'):
                environment_name = line.split(':')[1].strip()
                break

        if environment_name:
            print(f"The environment name is: {environment_name}")
        else:
            print("No Environment in this folder MT(maintenance).")

except FileNotFoundError:
    print("File not found.")

# maintenant on va elucider le path de l'environnement dont nous avons le nom
# sauf que je ne l'ai pas sur cet ordi. le mc. et que je ne l'ai pas encore crée.
# je voudrais inserer ici la commande qui permettra de creer un environnement avec {environment_name}
print(f'a partir de la , rien ne va plus, il va falloir y aller à pied...')

subprocess.run(["conda", "create", "--name", environment_name, "--yes"])


# ok maintenant l'etape qui fait tomber
# Activate the Conda environment
# une idee emerge. Parce que c apparemment impossible de lancer l activation avec python
# donc le fichier python va appeler un script


# Chemin vers le fichier d'activation de l'environnement Conda

# Nom de l'environnement Conda que vous souhaitez activer

# Commande pour activer l'environnement Conda
