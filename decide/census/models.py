from django.db import models
from django.contrib.auth.models import User

class Census(models.Model):
    voting_id = models.PositiveIntegerField()
    voter_id = models.ManyToManyField(User)

    class Meta:
        unique_together = (('voting_id'),)
