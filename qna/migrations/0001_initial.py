# Generated by Django 5.1.4 on 2024-12-25 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Date submitted')),
                ('slug', models.SlugField(unique=True)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('public', models.BooleanField(default=False)),
                ('allow_comments', models.BooleanField(default=True)),
            ],
        ),
    ]
