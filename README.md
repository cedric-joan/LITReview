# LITReview

Développer une application web en utilisant ``Django``.

Utiliser le rendu côté serveur dans Django.

Cette application web permettra à une communauté d'utilisateurs de consulter ou de solliciter une critique de livres à la demande.

# Fonctionnalités

* Se connecter et s'inscrire.
* Consulté un fil d'actulité des posts des utilisateurs auxquels on est abonné.
* Créer des tickets (demande de critique sur un livre/article).
* Créer des critiques, en réponse ou non à des tickets.
* Filtrer sur les tickets ou critiques avec la possibilité de les modifier ou les supprimer.
* Suivre d'autres utilisateurs, ou se désabonner.
* Voir qui l'on suit et par qui l'on est suivi.

# Tester le projet

Lancer votre terminal et clonez le projet:

    git clone https://github.com/cedric-joan/LITReview.git


# Installation

Pour faire fonctionner ce site web, suiver les instructions suivantes:
``Python version : 3.9``

Créer un environnement virtuel en utilisant la commande: ``python -m venv env``.

Pour l'activer exécutez la commande: env/bin/activate ou source env/Scripts/activate (sous Windows)

Les dépendances sont listés dans le fichier `requirements.txt`.

Lancer la commande: 
```
pip install -r requirements.txt
```

# Lancer le programme

Une fois dans le dossier src/ Lancer la commande:
```
python manage.py runserver
```

Une fois l'API lancée, allez sur votre navigateur internet préféré, à l'adresse suivante pour pouvoir acceder au site web:
```
http://127.0.0.1:8000/
```
Adresse administrateur:
```
http://127.0.0.1:8000/admin
```
Identifiant: patrick | Mot de passe : P@trick2023


