import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Patient

client = Client()

class ModelTestCase(TestCase):
    """A class that defines the test suite for the patient model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.valid_payload = {
            'first_name' : 'John',
            'middle_name' : 'Smith',
            'last_name' : 'Doe',
            'date_of_birth' : '2019-03-09',
            'gender' : 'M',
            'email' : 'john@doe.com',
            'phone' : '0724724724',
            'county' : 'Nairobi',
            'nhif' : '1234567890'
        }
        self.invalid_payload = {
            'first_name': '',
            'last_name' : 'Doe',
            'middle_name' : 'Smith',
            'date_of_birth' : '2019-03-09',
            'gender' : 'M',
            'email' : 'john@doe.com',
            'phone' : '0724724724',
            'county' : 'Nairobi',
            'nhif' : '1234567890'
        }
        client.post(
            "/api/v1/patients/",
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )

    def test_get_all_patient_records(self):
        """Test to check if all patient records can be retrieved"""
        response = client.get(
            "/api/v1/patients/",
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_patient_record(self):
        """Test to check if a patient record is created with valid data"""
        response = client.post(
            "/api/v1/patients/",
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_patient_record(self):
        """Test to check if a patient record can be created with invalid data"""
        response = client.post(
            "/api/v1/patients/",
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)