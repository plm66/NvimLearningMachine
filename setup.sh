#!/bin/zsh

# Lire conda env path du fichier 
conda_env_path=$(cat env_path.txt)

#source $conda_env_path/bin/activate
conda activate Lmachine

# Nettoyage du cache Conda
# echo "Cleaning Conda Cache..."
# conda clean --all -y 

# Installer les dépendances depuis le fichier venv_export.yml
#echo "Installing dependencies from venv_export.yml..."
#conda env update --file venv_export.yml


