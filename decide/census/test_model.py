import random
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from .models import Census
from voting.models import Voting, Question
from base.models import Auth
from base import mods
from base.tests import BaseTestCase

from django.contrib.auth.models import User

class CensusModelTestCase(TestCase):
    
    def setUp(self):

        user = User(username='prueba',password='prueba123')
        user.save()

        auth = Auth(name='prueba',url='localhost:8000')
        question = Question(desc='prueba')
        auth.save()
        question.save()
        voting = Voting(name='prueba',question=question)
        user.save()
        auth.save()
        question.save()
        voting.save()
        voting.auths.add(auth)
        voting.save()

        self.users = [user,]
        self.test_auths = [auth,]
        self.test_question = question
        self.test_census = Census(name='Prueba', voting_id=voting)
        self.test_census.save()
        self.test_census.voter_id.add(user)
        self.test_census.save()
    
    def test_get_census_by_id(self):
        self.assertEquals(self.test_census,self.test_census.get_by_id(1))
    
    def test_get_name_by_census(self):
        self.assertEquals('Prueba',self.test_census.get_name())

    def test_get_users_by_census(self):
        users = ['prueba',]
        result = []
        for data in self.test_census.get_users().all():
            result.append(data.username)
        self.assertEquals(users,result)
    
    def test_get_voting_by_census(self):
        self.assertEquals('prueba',self.test_census.get_voting().name)
        self.assertEquals('prueba',self.test_census.get_voting().question.desc)
    
    def test_tostring_census(self):
        self.assertEquals("Prueba:[prueba,['prueba']]",self.test_census.__unicode__())
    
    def tearDown(self):
        self.test_census.delete()