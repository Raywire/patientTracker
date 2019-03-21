import json
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from .models import Patient
from django.urls import reverse
from django.contrib.auth.models import User

class ModelTestCase(TestCase):
    """A class that defines the test suite for the patient model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.my_admin = User.objects.create(username='user')
        self.client = APIClient()
        user = User.objects.get()

        self.valid_payload = {
            'first_name' : 'John',
            'middle_name' : 'Smith',
            'last_name' : 'Doe',
            'date_of_birth' : '2019-03-09',
            'gender' : 'M',
            'email' : 'john@doe.com',
            'phone' : '0724724724',
            'county' : 'Nairobi',
            'id_number' : '1234567890'
        }
        self.valid_payload_2 = {
            'first_name' : 'John',
            'middle_name' : 'Smith',
            'last_name' : 'Doe',
            'date_of_birth' : '2019-03-09',
            'gender' : 'M',
            'email' : 'john@doe.com',
            'phone' : '0724724724',
            'county' : 'Nairobi',
            'id_number' : '12345678901'
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
            'id_number' : '1234567890'
        }
        self.valid_payload_appointment = {
            "title": "Eye Test",
            "attendant": "Doctor Doe",
            "description": "",
            "date_time": "2019-03-15T12:43",
            "patient": user.pk
        }
        self.valid_payload_2_appointment = {
            "title": "Eye Test",
            "attendant": "Doctor Doe",
            "description": "",
            "date_time": "2019-03-15T12:43",
            "patient": user.pk
        }

        self.invalid_payload_appointment = {
            "title": "Eye Test",
            "attendant": "Doctor Doe",
            "description": "",
            "date_time": "",
            "patient": user.pk
        }

        self.client.post(
            "/api/v1/patients/",
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )

    def test_get_all_patient_records(self):
        """Test to check if all patient records can be retrieved"""
        response = self.client.get(
            "/api/v1/patients/",
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_patient_record(self):
        """Test to check if a patient record is created with valid data"""
        response = self.client.post(
            "/api/v1/patients/",
            data=json.dumps(self.valid_payload_2),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_patient_record(self):
        """Test to check if a patient record can be created with invalid data"""
        response = self.client.post(
            "/api/v1/patients/",
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_a_specific_patient_record(self):
        """Test to check if a specific patient record can be retrieved."""
        patients = Patient.objects.get()
        response = self.client.get(
            reverse('patient-detail',
            kwargs={'pk': patients.pk}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_a_nonexistent_patient_record(self):
        """Test to check if a nonexistent patient record can be retrieved."""
        response = self.client.get(
            reverse('patient-detail',
            kwargs={'pk': 20}), format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_to_update_patient_record(self):
        """Test to update a patient record."""
        self.client.login(username='ryanwire', password='pt121212')
        patients = Patient.objects.get()
        res = self.client.put(
            reverse('patient-detail', kwargs={'pk': patients.id}),
            data=json.dumps(self.valid_payload_2) ,content_type='application/json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_to_delete_a_specific_patient_record(self):
        """Test to check if a specific patient record can be deleted."""
        
        patients = Patient.objects.get()
        response = self.client.delete(
            reverse('patient-detail',
            kwargs={'pk': patients.pk}), format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_to_delete_a_nonexistent_patient_record(self):
        """Test to check if a nonexistent patient record can be deleted."""
        response = self.client.delete(
            reverse('patient-detail',
            kwargs={'pk': 20}), format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_all_appointment_records(self):
        """Test to check if all appointments can be retrieved"""
        response = self.client.get(
            "/api/v1/appointments/",
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_patient_appointment(self):
        """Test to check if a patient appointment is created with valid data"""
        response = self.client.post(
            "/api/v1/appointments/",
            data=json.dumps(self.valid_payload_appointment),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
