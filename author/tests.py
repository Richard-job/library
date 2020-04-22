from django.test import TestCase
from .models import Author

# Create your tests here.

class AuthorTest(TestCase):
    def setUp(self):
        Author.obj.create(name='disney')

    def testGetByName(self):
        a1 = Author.obj.get(name='disney')

        self.assertEqual(a1.name, 'disney')

    def testUpdate(self):
        a1 = Author.obj.get(name='disney')
        a1.name = 'disnei'
        a1.save()

        a1 = Author.obj.get(name='disnei')
        self.assertEqual(a1.name, 'disnei')

    def testDelete(self):
        a1 = Author.obj.get(name='disney')
        a1.delete()

        a = Author.obj.all().count()
        self.assertEqual(a, 0)