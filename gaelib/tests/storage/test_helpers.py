from gaelib.defaults import (DEFAULT_STORAGE_BUCKET, APP_STORAGE_BUCKET)
from gaelib.tests.base import BaseUnitTestCase
from gaelib.storage import helpers
from gaelib.env import (get_app_or_default_prop)

class HelpersTestCase(BaseUnitTestCase):

  def setUp(self):
    super().setUp()

  def test_get_default_storage_bucket(self):
    self.assertEqual(helpers.get_default_storage_bucket(),
                     get_app_or_default_prop(DEFAULT_STORAGE_BUCKET))

  def test_get_storage_bucket(self):
    self.assertEqual(helpers.get_storage_bucket(),
                     get_app_or_default_prop(APP_STORAGE_BUCKET))
