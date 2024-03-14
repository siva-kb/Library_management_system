from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.db import models

#member’s outstanding debt is not more than Rs.500
class Member(models.Model):
    name = models.CharField(max_length=100)
    outstanding_debt = models.DecimalField(max_digits=10, decimal_places=2)

    def is_debt_within_limit(self):
        return self.outstanding_debt <= 500

class Book(models.Model):
    book_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    average_ratings = models.FloatField()
    isbn = models.CharField(max_length=13)
    isbn_13 = models.CharField(max_length=13, null=True, blank=True)
    language_code = models.CharField(max_length=40)
    num_pages = models.PositiveIntegerField()
    rating_count = models.FloatField()
    text_reviews_count = models.IntegerField()
    publication_date = models.DateField()
    publisher = models.CharField(max_length=30)

def __str__(self):
        return str(self.name) + " ["+str(self.isbn)+']'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classroom = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=3, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to="", blank=True)

    def __str__(self):
        return str(self.user) + " ["+str(self.branch)+']' + " ["+str(self.classroom)+']' + " ["+str(self.roll_no)+']'


def expiry():
    return datetime.today() + timedelta(days=14)
class IssuedBook(models.Model):
    student_id = models.CharField(max_length=100, blank=True) 
    isbn = models.CharField(max_length=13)
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)
