import os
import subprocess


def activate_conda_environment(environment_name):
    subprocess.run(['zsh', 'mt/activation_.sh', environment_name])
    print(f'Environnement {environment_name} activé avec succès.')
