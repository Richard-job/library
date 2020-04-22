from django.test import TestCase
from .models import Publisher

# Create your tests here.

class PublisherTest(TestCase):
    def setUp(self):
        Publisher.obj.create(name='disney')

    def testGetByName(self):
        p1 = Publisher.obj.get(name='disney')

        self.assertEqual(p1.name, 'disney')

    def testUpdate(self):
        p1 = Publisher.obj.get(name='disney')
        p1.name = 'dis'
        p1.save()

        p1 = Publisher.obj.get(name='dis')
        self.assertEqual(p1.name, 'dis')

    def testDelete(self):
        p1 = Publisher.obj.get(name='disney')
        p1.delete()

        p = Publisher.obj.all().count()
        self.assertEqual(p, 0)