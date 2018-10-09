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
    updated_ts = models.DateTimeField(auto_now=True)
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
    updated_ts = models.DateTimeField(auto_now=True)
    created_by = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'cdg_supported_drivers'


class InstalledDriver(models.Model):
    installed_drivers_seq = models.IntegerField(primary_key=True)
    supported_driver_seq = models.ForeignKey(SupportDriver, on_delete=models.CASCADE)
    installed_drivers_name = models.CharField(max_length=100)
    driver_version = models.CharField(max_length=30)
    driver_description = models.TextField()
    install_pip_cmd = models.CharField(max_length=50)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)
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
    updated_ts = models.DateTimeField(auto_now=True)
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
    updated_ts = models.DateTimeField(auto_now=True)
    created_by = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'cdg_established_connections'


class EstablishedSource(models.Model):
    established_sources_seq = models.IntegerField(primary_key=True)
    es_established_connections_seq = models.ForeignKey(EstablishedConnections, on_delete=models.CASCADE)
    es_name = models.CharField(max_length=50)
    es_source_type = models.CharField(max_length=50)
    es_schema = models.CharField(max_length=100)
    es_directory = models.CharField(max_length=200)
    es_connect_string = models.CharField(max_length=100)
    es_is_active = models.BooleanField(default=False)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)
    created_by = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'cdg_established_sources'


class EstablishedTarget(models.Model):
    established_target_seq = models.IntegerField(primary_key=True)
    et_established_connections_seq = models.ForeignKey(EstablishedConnections, on_delete=models.CASCADE)
    et_source_name = models.CharField(max_length=50)
    et_type = models.CharField(max_length=50)
    et_schema = models.CharField(max_length=100)
    et_directory = models.CharField(max_length=200)
    et_connect_string = models.CharField(max_length=100)
    et_is_active = models.BooleanField(default=False)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)
    created_by = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'cdg_established_target'

class ContentType(models.Model):
    content_type_seq = models.IntegerField(primary_key=True)
    content_type_name = models.CharField(max_length=50)
    content_type_short = models.CharField(max_length=100)
    content_type_long_description = models.TextField()
    content_type_is_active = models.BooleanField(default=False)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)
    created_by = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'cdg_content_type'


class DataSet(models.Model):
    dataset_seq = models.IntegerField(primary_key=True)
    dataset_name = models.CharField(max_length=50)
    dataset_established_sources_seq = models.ForeignKey(EstablishedSource, on_delete=models.CASCADE)
    dataset_content_type_seq = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    dataset_description = models.TextField()
    dataset_is_active = models.BooleanField(default=False)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)
    created_by = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'cdg_dataset'


class DatasetAttribute(models.Model):
    dataset_attribute_seq = models.IntegerField(primary_key=True)
    da_dataset_seq = models.ForeignKey(DataSet, on_delete=models.CASCADE)
    content_type_seq = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    dataset_attribute_name = models.CharField(max_length=100)
    da_source_col_seq = models.IntegerField()
    da_source_col_name = models.CharField(max_length=100)
    da_sample_col_data = models.CharField(max_length=100)
    da_source_col_type = models.CharField(max_length=100)
    is_pii_yn = models.CharField(max_length=100)
    da_source_col_size_1 = models.CharField(max_length=50)
    da_source_col_size_2 = models.CharField(max_length=50)
    da_source_col_short_desc = models.CharField(max_length=200)
    da_is_active = models.BooleanField(default=False)
    dataset_attributes_is_profiled = models.BooleanField(default=False)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)
    created_by = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'cdg_dataset_attribute'


class CurrentSchedule(models.Model):
    cs_seq = models.IntegerField(primary_key=True)
    cs_name = models.CharField(max_length=100)
    cs_command = models.CharField(max_length=200)
    cs_parameters = models.CharField(max_length=100)
    cs_runtime = models.CharField(max_length=50)
    cs_frequency = models.CharField(max_length=100)
    cs_description = models.TextField()
    cs_is_active = models.  BooleanField(default=False)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)
    created_by = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'cdg_current_schedules'


class CurrentScheduleActivities(models.Model):
    csa_seq = models.IntegerField(primary_key=True)
    cs_seq = models.ForeignKey(CurrentSchedule, on_delete=models.CASCADE)
    csa_name = models.CharField(max_length=100)
    csa_command = models.CharField(max_length=200)
    csa_parameters = models.CharField(max_length=100)
    csa_runtime = models.CharField(max_length=50)
    csa_frequency = models.CharField(max_length=100)
    csa_jobstatus = models.CharField(max_length=30)
    csa_job_starttime = models.DateTimeField(auto_now_add=True)
    csa_job_endtime = models.DateTimeField(auto_now=True)
    csa_job_run_duration = models.DateTimeField()
    csa_run_errors = models.CharField(max_length=200)
    csa_run_output = models.CharField(max_length=200)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)
    created_by = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'cdg_current_schedules_activities'


class DatasetLineage(models.Model):
    dataset_lineage_seq = models.IntegerField(primary_key=True)
    dl_dataset_seq = models.ForeignKey(DataSet, on_delete=models.CASCADE)
    dl_dataset_name = models.CharField(max_length=100)
    dl_dataset_type = models.CharField(max_length=200)
    dl_parent1_sources_seq = models.ForeignKey(EstablishedSource, on_delete=models.CASCADE)
    dl_child1_target_seq = models.ForeignKey(EstablishedTarget, on_delete=models.CASCADE)
    dl_content_type_seq = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    dl_comment = models.TextField()
    dl_is_active = models.BooleanField(default=False)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)
    created_by = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'cdg_dataset_lineage'


class SourceLineage(models.Model):
    source_lineage_seq = models.IntegerField(primary_key=True)
    sl_established_sources_seq = models.ForeignKey(EstablishedSource, on_delete=models.CASCADE)
    sl_source_name = models.CharField(max_length=100)
    # sl_parent1_source_seq = models.ForeignKey(EstablishedSource, on_delete=models.CASCADE)
    sl_content_type_seq = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    sl_comment = models.TextField()
    sl_is_active = models.BooleanField(default=False)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)
    created_by = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'cdg_source_lineage'


class Code(models.Model):
    code_seq = models.IntegerField(primary_key=True)
    code_type = models.CharField(max_length=100)
    code_name = models.IntegerField()
    code_value = models.IntegerField()
    code_description = models.TextField()
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)
    created_by = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'cdg_code'


class Functions(models.Model):
    functions_seq = models.IntegerField(primary_key=True)
    functions_name = models.CharField(max_length=100)
    functions_type = models.CharField(max_length=100)
    functions_description = models.TextField()
    functions_parameters = models.CharField(max_length=100)
    functions_is_active = models.BooleanField(default=True)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)
    created_by = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'cdg_functions'