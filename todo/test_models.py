from django.test import TestCase


class TestDjango(TestCase):

    def test_this_thing_work(self):
        self.assertEqual(1,1)

    def test_this_thing_work2(self):
        self.assertEqual(1,3)

    def test_this_thing_work3(self):
        self.assertEqual(1,)

    def test_this_thing_work4(self):
        self.assertEqual(1,4)