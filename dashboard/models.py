from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserLogger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    login_timestamp = models.DateTimeField(auto_now_add=True)
    logout_timestamp = models.DateTimeField(auto_now_add=True)
    login_hostname = models.TextField()
    login_ipaddress = models.TextField()
    comments = models.TextField()
    is_session_active = models.BooleanField(default=False)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(null=True)
    created_by = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'user_logger'

# class Connection(models.Model):