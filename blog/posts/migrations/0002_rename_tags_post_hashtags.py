# Generated by Django 4.1.6 on 2023-05-14 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="tags",
            new_name="hashtags",
        ),
    ]
