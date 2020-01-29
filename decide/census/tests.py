import random
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from .models import Census
from base import mods
from base.tests import BaseTestCase

from django.contrib.auth.models import User
from json import JSONEncoder
import datetime

'''
import unittest
from selenium import webdriver

Prueba test selenium

class TestSignup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def test_signup_fire(self):
        self.driver.get("http://localhost:8000/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("practica")
        self.driver.find_element_by_id('id_password').send_keys("practica")
        self.driver.find_element_by_id('login-form').click()
        self.assertTrue(len(self.driver.find_elements_by_id('user-tools'))>0) 
    def tearDown(self):
        self.driver.quit

if __name__ == '__main__':
    unittest.main()
'''

class MyEncoder(JSONEncoder):
        def default(self, o):
            o.date_joined = o.date_joined.__str__
            return o.__dict__

class CensusTestCase(BaseTestCase):

    def setUp(self):
        super().setUp()
        u = User.objects.get(username='admin')
        self.census = Census(voting_id=1)
        self.census.save()
        self.census.voter_id.add(u)
        self.census.save()

    def tearDown(self):
        super().tearDown()
        self.census = None

    def test_check_vote_permissions(self):
        response = self.client.get('/census/{}/?voter_id={}'.format(1, 10), format='json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), 'Invalid voter')

        response = self.client.get('/census/{}/?voter_id={}'.format(1, 1), format='json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), 'Invalid voter')

'''
    def test_list_census(self):
        response = self.client.get('census/listCensus')
        self.assertEqual(response.status_code, 200)
'''

    def test_list_voting(self):
        response = self.client.get('/census/?voting_id={}'.format(1), format='json')
        self.assertEqual(response.status_code, 401)

        self.login(user='noadmin')
        response = self.client.get('/census/?voting_id={}'.format(1), format='json')
        self.assertEqual(response.status_code, 403)

        self.login()
        response = self.client.get('/census/?voting_id={}'.format(1), format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'voters': [10]})
    
    def test_destroy_voter(self):
        u1 = User.objects.get(username='admin')
        data = {'voters': [u1.id]}
        response = self.client.delete('/census/{}/'.format(1), data, format='json')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(0, Census.objects.count())
        
"""
    def test_add_new_voters_conflict(self):
        u = User.objects.get(username='admin')
        data = {'voting_id': 1, 'voters': [u]}
        response = self.client.post('/census/', data, format='json')
        self.assertEqual(response.status_code, 401)

        self.login(user='noadmin')
        response = self.client.post('/census/', data, format='json')
        self.assertEqual(response.status_code, 403)

        self.login()
        response = self.client.post('/census/', data, format='json')
        self.assertEqual(response.status_code, 409)

    def test_add_new_voters(self):
        u1 = User.objects.get(username='admin')
        
        data = {'voting_id': 2, 'voters': [MyEncoder().encode(u1)]}
        response = self.client.post('/census/', data, format='json')
        self.assertEqual(response.status_code, 401)

        self.login(user='noadmin')
        response = self.client.post('/census/', data, format='json')
        self.assertEqual(response.status_code, 403)

        self.login()
        response = self.client.post('/census/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(data.get('voters')), Census.objects.count() - 1)
<<<<<<< HEAD
"""
