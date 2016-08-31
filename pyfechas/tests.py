from unittest import TestCase

from django.db import connections


class InfrastructureTest(TestCase):

    def test_db_connection(self):
        self.assertTrue(connections['default'].cursor())
