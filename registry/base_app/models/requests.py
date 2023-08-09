from django.db import models
from .variables import Variable


class Request(models.Model):
    """
    Request model is for store the variable requests database records
    """

    request_id = models.CharField(max_length=10, unique=True)

    # setup default status choices
    status_choices = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('DISAPPROVED', 'Disapproved'),
    )
    status = models.CharField(max_length=20, choices=status_choices,
                              default='PENDING')
    username = models.CharField(max_length=100)
    contact_email = models.EmailField()
    variables = models.ManyToManyField(Variable, related_name='requests')

    def __str__(self):
        return f"Request {self.request_id}"
