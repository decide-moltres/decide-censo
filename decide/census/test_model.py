import random
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from .models import Census
from base import mods
from base.tests import BaseTestCase

from django.contrib.auth.models import User

class CensusModelTestCase(TestCase):
    
    def setUp(self):

        user = User(username='prueba',password='prueba123')
        user.save()

        self.test_census = Census(voting_id=1)
        self.test_census.save()
        self.test_census.voter_id.add(user)
        self.test_census.save()
    
    def test_get_census_by_id(self):
        self.assertEquals(self.test_census,self.test_census.get_by_id(1))
    
    def test_get_users_by_census(self):
        self.assertEquals(self.test_census.voter_id,self.test_census.get_users())
    
    def test_get_voting_by_census(self):
        self.assertEquals(1,self.test_census.get_voting())
    
    def test_tostring_census(self):
        self.assertEquals('[1,{}]'.format(self.test_census.get_users),str(self.test_census))
    
    def tearDown(self):
        self.test_census.delete()