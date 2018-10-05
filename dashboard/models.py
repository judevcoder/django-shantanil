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
        db_table = 'cdg_user_logger'


class SupportDriver(models.Model):
    supported_driver_seq = models.IntegerField(primary_key=True)
    driver_official_pip_name = models.CharField(max_length=200)
    driver_description = models.TextField()
    driver_version = models.CharField(max_length=50)
    driver_for_source_system_name = models.CharField(max_length=100)
    driver_icon_path = models.FilePathField()
    driver_for_source_type = models.CharField(max_length=50)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(null=True)
    created_by = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'cdg_supported_drivers'


class InstalledDriver(models.Model):
    installed_drivers_seq = models.IntegerField(primary_key=True)
    supported_driver_seq = models.ForeignKey(SupportDriver, on_delete=models.CASCADE)
    installed_drivers_name = models.CharField(max_length=100)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(null=True)
    created_by = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'cdg_installed_drivers'


class DataStore(models.Model):
    datastore_seq = models.IntegerField(primary_key=True)
    datastore_installed_drivers_seq = models.ForeignKey(InstalledDriver, on_delete=models.CASCADE)
    datastore_name = models.CharField(max_length=100)
    datastore_host = models.CharField(max_length=50)
    datastore_port = models.CharField(max_length=50)
    datastore_directory = models.CharField(max_length=100)
    datastore_connection_type = models.CharField(max_length=50)
    ec_connection_success_flag = models.BooleanField(default=False)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(null=True)
    created_by = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'cdg_datastore'


class EstablishedConnections(models.Model):
    established_connections_seq = models.IntegerField(primary_key=True)
    ec_installed_drivers_seq = models.ForeignKey(InstalledDriver, on_delete=models.CASCADE)
    ec_datastore_seq = models.ForeignKey(DataStore, on_delete=models.CASCADE)
    ec_name = models.CharField(max_length=100)
    ec_userid = models.CharField(max_length=100)
    ec_password = models.CharField(max_length=200)
    ec_host = models.CharField(max_length=50)
    ec_port = models.CharField(max_length=50)
    ec_connectstring = models.CharField(max_length=200)
    ec_connection_type = models.CharField(max_length=50)
    ec_connection_success_flag = models.BooleanField(default=False)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(null=True)
    created_by = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'cdg_established_connections'



