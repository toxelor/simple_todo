from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Chel(AbstractUser):
    first_name = None
    last_name = None
    user_name = models.CharField(max_length=80)
    password = models.TextField()

    def create_user(self, username, password):
        self.username = username
        self.set_password(password)
        self.save()

    def create_note(self, text):
        note = Note()
        note.text = text
        note.chel = self
        note.save()

class Note(models.Model):
    text = models.TextField()
    #date = models.DateTimeField()
    chel = models.ForeignKey(Chel, on_delete=models.CASCADE)