import unittest
from password import Password

class TestPassword(unittest.TestCase):
    def setUp(self):

        self.new_password = Password("charles","maina","charles94","3094")

    def tearDown(self):
            Password.password_list = []
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

    def test_delete_passwords(self):
            self.new_password.save_password()
            test_password = Password("charles","maina","charles34","1234") 
            test_password.save_password()

            self.new_password.delete_passwords()
            self.assertEqual(len(Password.password_list),1)

    def test_display_all_passwords(self):
            self.assertEqual(Password.display_passwords(),Password.password_list)


if __name__ == '__main__':
    unittest.main()