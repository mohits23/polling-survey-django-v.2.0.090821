# Generated by Django 3.1.1 on 2021-01-25 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20210125_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizmodel',
            name='question',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
