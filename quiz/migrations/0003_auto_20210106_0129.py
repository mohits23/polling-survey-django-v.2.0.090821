# Generated by Django 3.1.1 on 2021-01-05 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20210106_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizmodel',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='quiz_images'),
        ),
    ]
