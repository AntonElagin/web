from django.test import TestCase
from .models import Creator

# Create your tests here.
class CreatorTestClass(TestCase):

    def SetUP(self):
        Creator.objects.create(username="testUsername1",name="zsxdfghjk",bio='qwe asd cx dfs asd',
                               email="test@mail.ru",password="fghkkh")
        Creator.objects.create(username="testUsername2", name="zsxdfghjk", bio='qwe asd cx dfs asd',
                               email="test@mail.ru", password="fghkkh")
        Creator.objects.create(username="testUsername3", name="zsxdfghjk", bio='qwe asd cx dfs asd', email="test@mail.ru",
                       password="fghkkh")

