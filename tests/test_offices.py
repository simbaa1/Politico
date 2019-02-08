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
        self.assertEqual(data["message"], 'office Created Successfully')
        self.assertEqual(resp.status_code, 201)

    def test_create_office_with_no_data(self):
        """Test when there is no data entered"""
        resp = self.client.post('api/v1/offices', content_type='application/json')
        data = resp.get_json()
        self.assertEqual(data['message'], 'No data has been entered')
        self.assertEqual(resp.status_code, 400)
    
    def test_create_office_with_missing_fields(self):
        """Test missing name field"""
        resp = self.client.post('api/v1/offices', content_type='application/json', json= {
                   
                   'type': 'Federal'
        })
        data = resp.get_json()
        self.assertEqual(data['message'], 'Cannot complete the request: Name field is missing')
        self.assertEqual(data['status'], 400)
        self.assertEqual(resp.status_code, 400)

    def test_create_office_already_exists(self):
        """Test when a office with a Similar Name already exist"""
        self.client.post('/api/v1/offices', content_type='application/json', json=self.office)
        resp = self.client.post('/api/v1/offices', content_type='application/json', json={
            'name': 'President',
            'type': 'Federal',
              }) 
        
        data = resp.get_json()
        self.assertEqual(data['message'], 'Cannot have offices with the same name')
        self.assertEqual(data['status'], 409)
        self.assertEqual(resp.status_code, 409)

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
        data = json.loads(resp.data.encode)
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['message'], 'Resource could not be retrieved')

    def test_delete_office(self):
        """Test deletion of a office by the DELETE request is successful"""
        
        resp = self.client.post('api/v1/offices',content_type='application/json', json=self.office)
        resp = self.client.delete('api/v1/offices/1')
        data = resp.get_json()
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'Deletion of the office was successful')
    
    def test_delete_office_no_office(self):
        resp =  self.client.delete('/api/v1/offices/2', content_type='application/json')
        data = json.loads(resp.data.encode)
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['message'], 'Resource could not be found')

    def tearDown(self):
        self.app = None
        self.office.clear()

    
if __name__ == '__main__':
    unittest.main()
