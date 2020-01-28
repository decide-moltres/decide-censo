from django.db import models
from django.contrib.auth.models import User
from voting.models import Voting

class Census(models.Model):
    name = models.CharField(max_length=50)
    voting_id = models.ForeignKey(Voting,on_delete=models.CASCADE)
    voter_id = models.ManyToManyField(User)

    class Meta:
        unique_together = (('name'),('voting_id'),)

    @classmethod
    def get_by_id(cls, cid):
        return Census.objects.get(pk=cid)
    
    def get_name(self):
        self.name=""
        return self.name

    def get_users(self):
        return self.voter_id

    def get_voting(self):
        return self.voting_id
    
    def __unicode__(self):
        users = []
        for data in self.get_users().all():
            users.append(data.username)
        return '{}:[{},{}]'.format(self.get_name(),self.get_voting().name,users)
