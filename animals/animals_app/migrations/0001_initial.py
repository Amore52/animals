# Generated by Django 5.2 on 2025-04-10 14:28

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('size', models.CharField(choices=[('tiny', 'tiny'), ('small', 'small'), ('medium', 'medium'), ('large', 'large')], max_length=6)),
                ('friendliness', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('trainability', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('shedding_amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('exercise_needs', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('color', models.CharField(max_length=50)),
                ('favorite_food', models.CharField(max_length=255)),
                ('favorite_toy', models.CharField(max_length=255)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals_app.breed')),
            ],
        ),
    ]
