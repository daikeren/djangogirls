from django.test import TestCase


class SimpleTest(TestCase):
    def testURLStatus(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        