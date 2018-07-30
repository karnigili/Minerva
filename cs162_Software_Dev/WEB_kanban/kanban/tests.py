import unittest
import requests
from requests import  Session
import random
import string



class TestFlaskApiUsingRequests(unittest.TestCase):
    def setUp(self):
        self.name = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
        self.mail = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))+'@gmail.com'
        self.password = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16))

    def test_home_redirect_not_login(self):
        '''
        tests redirection of non logged in users to login page
        '''
        r = requests.get('http://localhost:5000/')
        
        self.assertEqual(r.url, 'http://localhost:5000/login')


    def test_good_signup(self):
        '''
        tests a good sign up- using a random sign up details
        '''
        payload = {'email': self.mail, 'username':self.name, 'password':self.password}
        r = requests.post('http://localhost:5000/signup', data = payload) 

        self.assertEqual(r.url, 'http://localhost:5000/login')
        self.assertEqual(r.status_code, 200)

    
    def test_bad_login(self):
        '''
        tests a bad login with bad data
        '''
        payload = {'username':'gili', 'password':'ss'}
        r = requests.post('http://localhost:5000/login', data = payload)  
        
        self.assertEqual(r.url, 'http://localhost:5000/login')
        # self.assertEqual(r.status_code, 200)

    def test_good_login(self):
        '''
        tests a good login with known dummy user
        '''
        payload = {'username':'gili', 'password':'root'}
        r = requests.post('http://localhost:5000/login', data = payload)
        
        self.assertEqual(r.url, 'http://localhost:5000/board')

    def test_home_redirect_login(self):
        '''
        test redirecting to board when logged in
        '''
        s = Session()
        payload = {'username':'gili', 'password':'root'}
        req = s.post('http://localhost:5000/login', data = payload)
        r = s.get('http://localhost:5000/')

        self.assertEqual(r.url, 'http://localhost:5000/board')


    def test_logout(self):
        ''' 
        test log out
        '''
        
        r = requests.get('http://localhost:5000/logout')
        
        self.assertEqual(r.url, 'http://localhost:5000/login')


if __name__ == "__main__":
    unittest.main()

