import re
from datetime import date, datetime
import bcrypt
from django.db import models
from django.core.validators import EmailValidator, validate_email
from django.core.exceptions import ValidationError


class UserManager(models.Manager):
    def validate_registration(self, data):
        errors = {}

        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        email = data.get('email', '')
        password = data.get('password', '')
        confirm_password = data.get('confirm_password', '')

        if len(first_name) < 2:
            errors['first_name'] = "First name must be at least 2 characters long."
        elif not re.match(r'^[a-zA-Z]+$', first_name):
            errors['first_name'] = "First name must contain only letters."

        if len(last_name) < 2:
            errors['last_name'] = "Last name must be at least 2 characters long."
        elif not re.match(r'^[a-zA-Z]+$', last_name):
            errors['last_name'] = "Last name must contain only letters."

        if not self.is_email_valid(email):
            errors['email'] = "Invalid email format."

        if self.is_email_exists(email):
            errors['email'] = "Email already exists."

        if len(password) < 8:
            errors['password'] = "Password must be at least 8 characters long."
        if password != confirm_password:
            errors['confirm_password'] = "Passwords do not match."

        return errors
    
    def validate_login(self, data):
        errors = {}
        email = data.get('email', '')
        password = data.get('password', '')

        if not self.is_email_valid(email):
            errors['email'] = "Invalid email format."

        if not self.is_email_exists(email):
            errors['email'] = "Email does not exist."
        else:
            # check if password matches
            user = self.filter(email=email).first()
            if user and not bcrypt.checkpw(password.encode(), user.password.encode()):
                errors['password'] = "Incorrect password."

        return errors
    
    def is_email_valid(self, email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False
    
    def is_email_exists(self, email):
        return self.filter(email=email).exists()
    
    def register_user(self, data):
        errors = self.validate_registration(data)
        if errors:
            return (None, errors)
        
        password = data.get('password', '')
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            
        user = self.create(
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', ''),
            email=data.get('email', ''),
            password=hashed_password,
        )
        return (user, None)
    
    def login_user(self, data):
        errors = self.validate_login(data)
        if errors:
            return (None, errors)
        
        email = data.get('email', '')
        user = self.filter(email=email).first()
        return (user, None)


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # One-to-Many: User who uploaded this book
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    
    # Many-to-Many: Users who like this book
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    
    def __str__(self):
        return self.title