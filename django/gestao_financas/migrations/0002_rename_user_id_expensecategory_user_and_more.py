# Generated by Django 4.2 on 2023-05-20 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_financas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expensecategory',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='revenue',
            old_name='user_id',
            new_name='user',
        ),
    ]