# Generated by Django 4.2.6 on 2023-10-11 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tripplanning',
            name='budget',
        ),
        migrations.RemoveField(
            model_name='tripplanning',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='tripplanning',
            name='main_place',
        ),
        migrations.RemoveField(
            model_name='tripplanning',
            name='note',
        ),
        migrations.RemoveField(
            model_name='tripplanning',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='tripplanning',
            name='user',
        ),
        migrations.AlterField(
            model_name='tripplanning',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tripplanning',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='tripplanning',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='MainPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_place', models.CharField(blank=True, max_length=20, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('place_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('note', models.TextField(blank=True, null=True)),
                ('budget', models.IntegerField(blank=True, null=True)),
                ('trip_planning', models.ManyToManyField(to='travel_manager.tripplanning')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]