# Generated by Django 5.0.3 on 2024-03-14 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_post', '0001_initial'),
        ('core_user', '0003_user_avatar_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='posts_liked',
            field=models.ManyToManyField(related_name='liked_by', to='core_post.post'),
        ),
    ]
