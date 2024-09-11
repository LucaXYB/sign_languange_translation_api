from django.test import TestCase, Client
from django.urls import reverse
import json

# Create your tests here.
class TranslateTextTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('translate_text')

    def test_translation_success(self):
        """
            Test the case where the translation is successful.
        """
        response = self.client.post(self.url, data=json.dumps({"text": "hello"}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {
            "input_text": "hello",
            "translated_text": "hello (translated)",
            "message": "Translation successful"
        })

    def test_no_text_provided(self):
        """
            Test the case where no text provided in the request
        """
        response = self.client.post(self.url, data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {"error": "No text provided"})

    def test_invalid_json(self):
        """
        Test the case where invalid JSON is sent in the request.
        """
        response = self.client.post(self.url, data="invalid json", content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {"error": "Invalid JSON"})

    def test_invalid_method(self):
        """
        Test the case where a method other than POST is used.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 405)
        self.assertJSONEqual(response.content, {"error": "Invalid method"})