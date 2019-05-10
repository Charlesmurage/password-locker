import unittest
from password import password

class TestPassword = (unittest.TestCase):
    def setUp(self):
        self.new_password = Password("charles","maina","charles94","3094")

    def test_init(self):
        self.assertEqual(self.new_password.first_name,"charles")
        self.assertEqual(self.new_password.last_name,"maina")
        self.assertEqual(self.new_password.user_name,"charles94")
        self.assertEqual(self.new_password.password,"3094")

if __name__ == '__main__':
    unittest.main()