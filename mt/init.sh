#!/bin/zsh
echo "Initialisation de Conda dans le shell actuel..."
conda init $(basename "$SHELL")
echo "Conda a été initialisé avec succès."
if [ "$(basename "$SHELL")" = "zsh" ]; then
  echo "Chargement de la configuration Zsh..."
  source ~/.zshrc
  echo "Configuration Zsh chargée avec succès."
  source ~/.bash_profile
  echo "Configuration bash_profile chargée avec succès."




fi

