import os
import django

# Configuration de l'environnement Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

email = 'benji@gmail.com'
password = 'nagatopain'
username = 'benji'

if not User.objects.filter(email=email).exists():
    user = User.objects.create_user(username=username, email=email, password=password)
    print(f"Utilisateur {email} créé avec succès !")
else:
    user = User.objects.get(email=email)
    user.set_password(password)
    user.save()
    print(f"Le mot de passe de l'utilisateur {email} a été mis à jour.")
