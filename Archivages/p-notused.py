import os
import subprocess

# Récupérer la variable d'environnement CONDA_PREFIX qui contient le chemin vers l'environnement Conda actif
conda_env_path = os.getenv('CONDA_PREFIX')

activate_command = '. {}/bin/activate'.format(conda_env_path)
os.system(activate_command)

install_dependencies_command = 'conda env update --file venv_export.yml'
subprocess.run(install_dependencies_command, shell=True)
