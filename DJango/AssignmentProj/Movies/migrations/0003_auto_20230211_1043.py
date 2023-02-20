# Generated by Django 4.1.6 on 2023-02-11 05:13

from django.db import migrations


class Migration(migrations.Migration):

    def insertData(apps, schema_editor):
        MoviesList = apps.get_model('Movies', 'MoviesList')
        movie = MoviesList(title = "The Hulk", desc = "Marvel Franchise", release_date = "2008-08-09", num_actors = 10, upvotes = 1000, downvotes= 5)
        movie.save()

    dependencies = [
        ('Movies', '0002_alter_movieslist_id'),
    ]

    operations = [
        migrations.RunPython(insertData),
    ]
