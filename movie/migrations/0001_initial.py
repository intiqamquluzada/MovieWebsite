# Generated by Django 3.2 on 2023-01-26 21:41

from django.db import migrations, models
import services.uploader


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Comedy', 'Comedy'), ('Adventure', 'Adventure'), ('Tragedy', 'Tragedy'), ('Action', 'Action'), ('Love', 'Love')], max_length=200)),
                ('rating', models.IntegerField()),
                ('image', models.ImageField(upload_to=services.uploader.Uploader.upload_images_to_movies)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]