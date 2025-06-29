# Generated by Django 5.2.3 on 2025-06-14 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_customuser_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]
