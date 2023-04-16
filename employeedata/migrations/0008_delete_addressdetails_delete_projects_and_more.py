# Generated by Django 4.2 on 2023-04-07 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeedata', '0007_employeedata_regid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AddressDetails',
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
        migrations.DeleteModel(
            name='Qualification',
        ),
        migrations.DeleteModel(
            name='WorkExperience',
        ),
        migrations.RemoveField(
            model_name='employeedata',
            name='addressDetails',
        ),
        migrations.RemoveField(
            model_name='employeedata',
            name='phoneNo',
        ),
        migrations.RemoveField(
            model_name='employeedata',
            name='qualificiations',
        ),
        migrations.RemoveField(
            model_name='employeedata',
            name='workExeperience',
        ),
        migrations.AddField(
            model_name='employeedata',
            name='address_details',
            field=models.TextField(blank=True, null=True, verbose_name='addressdetails'),
        ),
        migrations.AddField(
            model_name='employeedata',
            name='phone_no',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='phone_no'),
        ),
        migrations.AddField(
            model_name='employeedata',
            name='qualifications',
            field=models.TextField(blank=True, null=True, verbose_name='qualifications'),
        ),
        migrations.AddField(
            model_name='employeedata',
            name='work_exeperience',
            field=models.TextField(blank=True, null=True, verbose_name='workexeperience'),
        ),
    ]
