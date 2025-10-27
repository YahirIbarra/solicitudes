from django.test import TestCase

class TestSmokeTest(TestCase):

    def test_hola_mundo(self):
        self.assertEqual('hola mundo', 'hola mundo')
