# Generated by Django 3.2 on 2023-01-26 22:26

from django.db import migrations, models
import django.db.models.deletion
import services.uploader


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20230126_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cast_of_Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=services.uploader.Uploader.upload_images_for_cast)),
                ('position', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='movie',
            name='cast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.cast_of_movie'),
        ),
    ]