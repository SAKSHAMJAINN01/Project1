# Generated by Django 3.2.10 on 2024-04-14 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_alter_author_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='upvotes',
        ),
        migrations.AddField(
            model_name='userpost',
            name='category',
            field=models.CharField(max_length=25, null=True),
        ),
    ]