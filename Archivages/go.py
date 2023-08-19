import os
import subprocess

# Lancer g.py 
subprocess.run(['python', './g.py'], check=True)

# Exécuter setup.sh pour activer environement conda et installer dependences.
subprocess.run(['./setup.sh'], check=True)
