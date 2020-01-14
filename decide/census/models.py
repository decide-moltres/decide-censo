from django.db import models
from django.contrib.auth.models import User

class Census(models.Model):
    voting_id = models.PositiveIntegerField()
    voter_id = models.ManyToManyField(User)

    class Meta:
        unique_together = (('voting_id'),)

    @classmethod
    def get_by_id(cls, cid):
        return Census.objects.get(pk=cid)

    def get_users(self):
        return self.voter_id

    def get_voting(self):
        return self.voting_id
    
    def __unicode__(self):
        return '[{},{}]'.format(self.voting_id,self.voter_id)