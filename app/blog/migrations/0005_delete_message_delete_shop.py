# Generated by Django 4.0 on 2021-12-12 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_message_alter_article_id_alter_comment_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
    ]
