import unittest
import os
import json
from app import create_app

class OfficeTestCase(unittest.TestCase):
    """Class for testing an office"""

    def setUp(self):
        """Initialze app and define variables for the test"""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.office = {
            
            'name': 'President',
            'type': 'federal'
        }

    def test_create_office(self):
        """Test the POST request for create office"""
        resp = self.client.post('/api/v1/offices', content_type='application/json', json=self.office)
        data = resp.get_json()
        self.assertEqual(data["message"], 'Office Created Successfully')
        self.assertEqual(resp.status_code, 201)

    def test_create_office_with_no_data(self):
        """Test when there is no data entered"""
        resp = self.client.post('api/v1/offices', content_type='application/json')
        data = resp.get_json()
        self.assertEqual(data['message'], 'Some fields are missing')
        self.assertEqual(data['status'], 400)
        self.assertEqual(resp.status_code, 400)
    
    def test_create_office_with_missing_fields(self):
        """Test missing name field"""
        resp = self.client.post('api/v1/offices', content_type='application/json', json= {
                   
                   'type': 'Federal'
        })
        data = resp.get_json()
        self.assertEqual(data['message'], 'Some fields are missing')
        self.assertEqual(data['status'], 400)
        self.assertEqual(resp.status_code, 400)

    def test_get_all_offices(self):
        """Test GET request for all offices"""
        resp = self.client.post('/api/v1/offices', content_type='application/json', json=self.office)
        
        self.assertEqual(resp.status_code, 201)
        resp = self.client.get('/api/v1/offices')
        data = resp.get_json()
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'Request was successful')
    
    def test_get_office_by_id(self):
        """ Test GET request API to retrieve a office based on its id"""

        self.client.post('/api/v1/offices', content_type='application/json', json=self.office)
        resp = self.client.get('/api/v1/offices/1')
        data = resp.get_json()
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertTrue(data['data'][0]['name'], "President")
        self.assertEqual(data['message'], 'Request was successful')
        
    
    def test_no_office_returned(self):
        """ Test GET request when and ID does not return any office """

        resp =  self.client.get('/api/v1/offices/23', content_type='application/json')
        data = resp.get_json()
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['message'], 'Resource could not be retrieved')


    def tearDown(self):
        self.app = None
        self.office.clear()

    
if __name__ == '__main__':
    unittest.main()
