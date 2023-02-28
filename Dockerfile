# Utilisez une image de base Python
FROM python:3.9-slim-buster

# Définissez le répertoire de travail dans l'image
WORKDIR /app

# Copiez le fichier requirements.txt dans l'image

# Installez les dépendances du projet


# Copiez tous les fichiers de l'application dans l'image
COPY . .

# Exposez le port sur lequel votre application écoute
EXPOSE 9000

# Définissez la commande pour lancer l'application
CMD ["python", "lib.py"]
