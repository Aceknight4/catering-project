import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catering.settings')
django.setup()

from django.contrib.auth.models import User

username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email    = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@elitecatering.cm')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'Admin1234!')

if User.objects.filter(username=username).exists():
    u = User.objects.get(username=username)
    u.set_password(password)
    u.is_staff = True
    u.is_superuser = True
    u.save()
    print(f"Password reset for {username}")
else:
    User.objects.create_superuser(username, email, password)
    print(f"Superuser {username} created")
