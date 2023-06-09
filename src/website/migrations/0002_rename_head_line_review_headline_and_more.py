# Generated by Django 4.1.7 on 2023-04-02 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='head_line',
            new_name='headline',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='uploader',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='image',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
