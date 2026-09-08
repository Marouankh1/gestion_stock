# 📦 Plateforme de Gestion de Stock (Django)

Application web de gestion de stock développée avec **Python** et **Django**, utilisant **Bootstrap 5** pour l'interface utilisateur.

## 🚀 Installation & Lancement (Pour commencer)

Si vous téléchargez ce projet pour la première fois, suivez ces étapes dans votre terminal :

### 1. Cloner le projet
```bash
git clone <URL_DE_VOTRE_REPO>
cd gestion_stock

```

### 2. Créer et activer l'environnement virtuel

* **Sur Windows (Git Bash / CMD):**
```bash
python -m venv venv
source venv/Scripts/activate  # ou venv\Scripts\activate

```


* **Sur Mac / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate

```



### 3. Installer les dépendances

```bash
pip install django

```

### 4. Appliquer les migrations de la base de données

```bash
python manage.py makemigrations
python manage.py migrate

```

### 5. Créer un compte administrateur (Superuser)

```bash
python manage.py createsuperuser

```

*(Suivez les instructions pour entrer un nom d'utilisateur, un email et un mot de passe).*

### 6. Lancer le serveur local

```bash
python manage.py runserver

```

Ouvrez ensuite votre navigateur et allez sur : `http://127.0.0.1:8000/`