# Generated by Django 3.1.1 on 2020-10-30 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_bookinstance_borrower'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='book_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
