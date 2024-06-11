# Utiliser une image de base légère
FROM python:3.10-alpine

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application dans le répertoire de travail
COPY . .

# Exposer le port sur lequel l'application s'exécute
EXPOSE 5000

# Définir la variable d'environnement pour le port
ENV PORT 5000

# Lancer l'application en mode développement
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
