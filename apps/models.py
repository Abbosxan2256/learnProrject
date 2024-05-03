from django.db.models import EmailField, DateTimeField, DateField, Model, ImageField, CharField


class Person(Model):
    photo = ImageField()
    name = CharField(max_length=255)
    location = CharField(max_length=255)
    job = CharField(max_length=255)
    birth_day = DateField()
    create_at = DateTimeField(auto_now_add=True)
