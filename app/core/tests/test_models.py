from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        """Test creating a new user with a new email"""
        email = 'rax.wer@gmail.com'
        password = 'raxwer'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the email for the new user is normalized"""
        email = 'rax.wer@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'abc')

    def test_create_new_super_user(self):
        """Test if super user created"""
        user = get_user_model().objects.create_super_user(
            'test@asdasd.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
