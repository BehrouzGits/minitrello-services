# Generated by Django 5.0.4 on 2024-06-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_otprequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otprequest',
            name='channel',
            field=models.CharField(choices=[('Phone', 'Phone'), ('E-Mail', 'Email')], default='Phone', max_length=10),
        ),
    ]
