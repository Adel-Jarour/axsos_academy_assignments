import re
from datetime import date, datetime
import bcrypt
from django.db import models
from django.core.validators import EmailValidator, validate_email
from django.core.exceptions import ValidationError

# Create your models here.

class UserManager(models.Manager):
    def validate_registration(self, data):
        errors = {}

        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        email = data.get('email', '')
        password = data.get('password', '')
        confirm_password = data.get('confirm_password', '')
        birthday_str = data.get('birthday', '')

        # Parse birthday string (from HTML date input) into a date object
        birthday = None
        if birthday_str:
            try:
                birthday = datetime.strptime(birthday_str, '%Y-%m-%d').date()
            except (ValueError, TypeError):
                pass  # handled below as missing/invalid

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

        # Birthday validation (NINJA BONUS)
        if not birthday:
            errors['birthday'] = "Birthday is required."
        else:
            # check if date is in the past
            if birthday > date.today():
                errors['birthday'] = "Birthday must be in the past."
            else:
                # check if user is at least 13 years old
                today = date.today()
                age = today.year - birthday.year
                # Adjust if birthday hasn't occurred yet this year
                if today.month < birthday.month or (today.month == birthday.month and today.day < birthday.day):
                    age -= 1

                if age < 13:
                    errors['birthday'] = "You must be at least 13 years old to register."
        
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
            birthday=data.get('birthday', None)
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
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    birthday = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"