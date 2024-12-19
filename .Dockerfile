 # Utiliser une image Python comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de votre application dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Exposer le port utilisé par Streamlit
EXPOSE 8501

# Définir la commande pour démarrer l'application
CMD ["streamlit", "run", "app/loan_app.py", "--server.port=8501", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]
