from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user, _ = User.objects.get_or_create(email='admin@django.com')
        if _:
            user.is_superuser = True
            user.is_staff = True
            user.set_password('password')
            user.save()
        else:
            print("Добро пожаловать!")
