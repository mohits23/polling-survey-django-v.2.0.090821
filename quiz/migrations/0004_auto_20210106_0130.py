# Generated by Django 3.1.1 on 2021-01-05 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20210106_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizmodel',
            name='image',
            field=models.ImageField(null=True, upload_to='quiz_images'),
        ),
    ]
