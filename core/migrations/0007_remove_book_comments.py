# Generated by Django 4.0.4 on 2022-07-07 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_book_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='comments',
        ),
    ]
