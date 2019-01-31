from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASS_REGEX = re.compile(r'^\d.*[A-Z]|[A -Z].*\d')

# Create your models here.
class UsersManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}

        if len(postData['email']) < 1:
            errors['email'] = "Email cannot be left blank."
        elif len(Users.objects.filter(email=postData['email'])) > 0:
            errors['email'] = "That email has already been registered. Please try another email."
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address."
        
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters long."
        elif not PASS_REGEX.match(postData['password']):
            errors['password'] = "Password must contain at least one uppercase letter and at least one number."
        
        if postData['password'] != postData['pw_confirm']:
            errors['pw_confirm'] = "Passwords do not match. Please try again."
        
        return errors

    def log_validator(self, postData):
        errors = {}

        if len(Users.objects.filter(email=postData['email'])) < 1:
            errors['email'] = "Invalid email, try again."
        
        else:
            user = Users.objects.get(email=postData['email'])
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['password'] = "Invalid password, please try again."
       
        return errors


class Users(models.Model):
    u_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UsersManager()

    def __str__(self):
        return ' '.join([
            self.u_name,
            self.email
        ])
