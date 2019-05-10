import unittest
from password import Password

class TestPassword(unittest.TestCase):
    def setUp(self):
        self.new_password = Password("charles","maina","charles94","3094")

    def test_init(self):
        self.assertEqual(self.new_password.first_name,"charles")
        self.assertEqual(self.new_password.last_name,"maina")
        self.assertEqual(self.new_password.user_name,"charles94")
        self.assertEqual(self.new_password.password,"3094")

    def test_save_password(self):
        self.new_password.save_password()
        self.assertEqual(len(Password.password_list),1)

    def test_save_mulitple_password(self):
        self.new_password.save_password()
            test_password = Password("charles","maina","charles34","1234") 
            test_password.save_password()
            self.assertEqual(len(Password.password_list),2)


if __name__ == '__main__':
    unittest.main()