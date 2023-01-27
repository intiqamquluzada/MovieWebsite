# Generated by Django 3.2 on 2023-01-26 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_rename_cast_movie_movie_cast'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='movie_cast',
            new_name='people',
        ),
        migrations.AddField(
            model_name='cast_of_movie',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='cast_of_movie',
            name='slug',
            field=models.SlugField(default='e', editable=False, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cast_of_movie',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
