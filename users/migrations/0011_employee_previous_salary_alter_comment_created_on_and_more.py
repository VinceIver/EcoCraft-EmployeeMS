# Generated by Django 4.2.7 on 2023-11-17 08:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_comment_created_on_alter_employee_pub_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='previous_salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 17, 8, 1, 32, 265687, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 17, 8, 1, 32, 265687, tzinfo=datetime.timezone.utc)),
        ),
    ]
