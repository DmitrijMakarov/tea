from django.test import TestCase, Client

class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        response_admin = self.client.get('/admin/')
        response_blogs = self.client.get('/blogs/')
        response_delivery = self.client.get('/delivery/')
        response_login = self.client.get('/login/')
        response_card_product = self.client.get('/card_product/')
        response_logout = self.client.get('/logout/')
        response_index = self.client.get('')

        self.assertEqual(response_admin.status_code, 200)
        self.assertEqual(response_blogs.status_code, 200)
        self.assertEqual(response_delivery.status_code, 200)
        self.assertEqual(response_login.status_code, 200)
        self.assertEqual(response_card_product.status_code, 200)
        self.assertEqual(response_logout.status_code, 200)
        self.assertEqual(response_index.status_code, 200)
