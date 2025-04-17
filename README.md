# 📝 Blog avec Django

Bienvenue dans ce projet de blog développé avec le framework web Django.  
Ce projet permet de publier, consulter et gérer des articles depuis une interface utilisateur conviviale.

## 🚀 Fonctionnalités

- 📰 Création, édition et suppression d'articles
- 🔐 Authentification et autorisation des utilisateurs
- 🖼️ Téléversement d’images (miniatures)
- 📆 Gestion des dates de création et de mise à jour
- 🌐 Interface publique pour la lecture des articles
- 🎛️ Interface admin Django pour gérer les articles



## ⚙️ Prérequis

- Python 3.13
- Django 5.2
- pip
- Git
- Un environnement virtuel (fortement recommandé)

## 📦 Installation

```bash
# Cloner le projet
git clone https://github.com/<TON-UTILISATEUR>/blog-avec-django.git
cd blog-avec-django

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate   # Sur Windows : venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Lancer les migrations
python manage.py migrate

# Créer un super utilisateur
python manage.py createsuperuser

# Lancer le serveur de développement
python manage.py runserver
```

## 👤 Auteur

- Nom : **TAMETONG Paul**
- Contact : mesbus8@gmail.com

