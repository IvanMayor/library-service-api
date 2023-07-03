from django.conf import settings
from django.db import models


class Book(models.Model):
    book_cover_choices = [
        ("HARD", "HARD"),
        ("SOFT", "SOFT"),
    ]
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.CharField(
        max_length=4,
        choices=book_cover_choices,
    )
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return f"{self.title}-{self.author}"


class Borrowing(models.Model):
    borrow_date = models.DateField(auto_now_add=True)
    expected_return = models.DateField()
    actual_return = models.DateField(blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="books")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}-{self.borrow_date}"


