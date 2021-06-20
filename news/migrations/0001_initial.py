# Generated by Django 3.2.3 on 2021-05-30 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=None, verbose_name='Название')),
                ('subtitle', models.CharField(max_length=250, null=None, verbose_name='Заголовок')),
                ('text', models.TextField(null=None, verbose_name='Содержание')),
                ('date', models.DateTimeField(null=None, verbose_name='Дата')),
            ],
        ),
    ]