import os

# Récupérer la variable d'environnement CONDA_PREFIX qui contient le chemin vers l'environnement Conda actif
conda_env_path = os.getenv('CONDA_PREFIX')

# Écrire ce chemin dans un fichier 
with open('env_path.txt', 'w') as f:
    f.write(conda_env_path)
