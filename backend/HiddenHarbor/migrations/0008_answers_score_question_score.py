# Generated by Django 4.2.1 on 2023-12-11 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HiddenHarbor', '0007_question_allowprivatemessages'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
