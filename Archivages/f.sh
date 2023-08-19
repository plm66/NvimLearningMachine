

#!/bin/zsh

# Path to the virtual environment
venv_path="$PWD/.venv"

# Activate the virtual environment
source "$venv_path/bin/activate"

# Install the dependencies from the requirements.txt file
pip install -r requirements.txt





# ce fichier est la pour me permettre d'activer le même environnement quand j'ouvre une nouvelle fenetre du terminal. Parce que c penible a chaque fois, de se taper les appels de configuration.
# Mais attention ici on est sur du conda exclusivement.
# On se rappellera :
#
# conda install --file requirements /// pour eviter la confusion avec un package qui s 'intitulerait requirements


