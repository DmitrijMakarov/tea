from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

import random



class Profile(models.Model):
    pass


class Vote(models.Model):
    pass

class User_c(User):
    is_verified = models.BooleanField(default=False)
    votings_created = models.IntegerField(default=0)
    votings_complited_counter = models.IntegerField(default=0)

