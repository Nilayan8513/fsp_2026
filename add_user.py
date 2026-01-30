import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'day2.settings')
django.setup()

from mysite.models import users

# Check if user already exists
try:
    user = users.objects.get(email='admin2@a.com')
    print(f"User already exists: {user.name} - {user.email}")
except users.DoesNotExist:
    # Create new user
    new_user = users(
        name='Sonu',
        email='admin2@a.com',
        age=25,
        pwd='admin',
        phno=9999999999
    )
    new_user.save()
    print(f"User created successfully: {new_user.name} - {new_user.email}")
