# Generated by Django 4.1.7 on 2023-04-18 15:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_ticket_image_delete_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(blank=True, max_length=5000, verbose_name='Commentaire'),
        ),
        migrations.AlterField(
            model_name='review',
            name='headline',
            field=models.CharField(max_length=128, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Note(0 - 5)'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Contenu'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Titre'),
        ),
    ]
