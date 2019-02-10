import unittest
import os
import json
from app import create_app


class PartyTestCase(unittest.TestCase):
    """Class for testing a party"""

    def setUp(self):
        """Initialze app and define variables for the test"""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.party = {

            'name': 'ODM',
            'hq_address': 'Upperhill',
            'logo_url': 'www.pixabay.com/images',
            'chairperson': 'Maikol'
        }

    def test_create_party(self):
        """Test the POST request for create party"""
        resp = self.client.post('/api/v1/parties', content_type='application/json', json=self.party)
        data = resp.get_json()
        self.assertEqual(data['message'], 'Party Created Successfully')
        self.assertEqual(data['status'], 201)
        self.assertEqual(resp.status_code, 201)

    def test_create_party_with_no_data(self):
        """Test when there is no data entered"""
        resp = self.client.post('api/v1/parties', content_type='application/json', json={})
        data = resp.get_json()
        self.assertEqual(data['message'], 'Some field(s) are missing')
        self.assertEqual(resp.status_code, 400)
    
    def test_create_party_with_missing_fields(self):
        """Test missing name field"""
        resp = self.client.post('api/v1/parties', content_type='application/json', json= {
                   
                   'hq_address': 'Upperhill',
                   'logo_url': 'www.pixabay.com/images',
                   'chairperson': 'Maikol'
        })
        data = resp.get_json()
        self.assertEqual(data['message'], 'Some field(s) are missing')
        self.assertEqual(data['status'], 400)
        self.assertEqual(resp.status_code, 400)


    def test_get_all_parties(self):
        """Test GET request for all parties"""
        resp = self.client.post('/api/v1/parties', content_type='application/json', json=self.party)
        
        self.assertEqual(resp.status_code, 201)
        resp = self.client.get('/api/v1/parties')
        data = resp.get_json()
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'Request was successful')
    
    def test_get_party_by_id(self):
        """ Test GET request API to retrieve a party based on its id"""

        self.client.post('/api/v1/parties', content_type='application/json', json=self.party)
        resp = self.client.get('/api/v1/parties/1')
        data = resp.get_json()
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertTrue(data['data'][0]['name'], "ODM")
        self.assertEqual(data['message'], 'Request was successful')
        
    
    def test_no_party_returned(self):
        """ Test GET request when and ID does not return any party """

        resp =  self.client.get('/api/v1/parties/23', content_type='application/json')
        data = resp.get_json()
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['message'], 'Resource could not be found')

    def test_delete_party(self):
        """Test deletion of a party by the DELETE request is successful"""
        
        resp = self.client.post('api/v1/parties',content_type='application/json', json=self.party)
        resp = self.client.delete('api/v1/parties/1')
        data = resp.get_json()
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['status'], 200)
        
    
    def test_delete_party_no_party(self):
        resp =  self.client.delete('/api/v1/parties/32', content_type='application/json')
        data = resp.get_json()
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['message'], 'Resource could not be found')

    def test_patch_party(self):
        """Test editing of a party name by the PATCH request is successful"""
        
        resp = self.client.post('api/v1/parties',content_type='application/json', json=self.party)
        resp = self.client.patch('api/v1/parties/1/CORD')
        data = resp.get_json()
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'Pary name was succesfully updated')
        self.assertEqual(data['data'][0]['name'], 'CORD')
        self.assertEqual(data['data'][0]['id'], 1)

    def test_patch_party_no_party(self):
        resp =  self.client.patch('/api/v1/parties/2/CORD', content_type='application/json')
        data = resp.get_json()
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['message'], 'Resource could not be found')

    def tearDown(self):
        self.app = None
        self.party.clear()

    
if __name__ == '__main__':
    unittest.main()
