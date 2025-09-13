# 📝 Citations Flask

Mini application **Flask (Python)** qui affiche des citations aléatoires.  
Le projet est **dockerisé** et prêt à être déployé sur [Render](https://render.com) ou tout autre hébergeur compatible Docker.

---

## 🚀 Fonctionnalités
- Affiche une citation aléatoire à chaque clic sur le bouton.
- Frontend en **HTML / CSS / JS** (design sombre + animation).
- Backend en **Python Flask**.
- Conteneurisé avec **Docker**.

---

## 📂 Structure du projet
```
citations-flask/
│── app.py              # Application Flask
│── requirements.txt    # Dépendances Python
│── Dockerfile          # Image Docker
│── quotes.json         # Citations stockées en local
│
├── templates/
│   ├── base.html
│   └── index.html
│
└── static/
    ├── style.css
    └── app.js
```

---

## 🐳 Lancer avec Docker

### 1. Construire l’image
```bash
docker build -t citations-flask .
```

### 2. Lancer le conteneur
```bash
docker run -p 5001:5000 citations-flask
```

👉 L’application sera accessible sur [http://127.0.0.1:5001](http://127.0.0.1:5001).

---

## 💻 Lancer en local (sans Docker)

### 1. Créer un environnement virtuel
```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.\.venv\Scriptsctivate    # Windows PowerShell
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Lancer l’application
```bash
python app.py
```

👉 L’application sera accessible sur [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## 🌍 Déploiement
- Déployable sur **Render** en quelques clics (Web Service → Docker).  
- Fonctionne aussi sur **Railway, Fly.io, Heroku (Docker)**.  

---

## 🏷️ Technologies
- Python 3.11  
- Flask  
- HTML / CSS / JavaScript  
- Docker  
