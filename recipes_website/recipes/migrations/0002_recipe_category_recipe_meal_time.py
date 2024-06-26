# Generated by Django 4.2.5 on 2024-04-01 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('HEALTH_DIET', 'Health & Diet'), ('HOLIDAYS', 'Holidays')], default='HEALTH_DIET', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='meal_time',
            field=models.CharField(choices=[('BREAKFAST', 'Breakfast'), ('LUNCH', 'Lunch'), ('DINNER', 'Dinner')], default='BREAKFAST', max_length=100),
            preserve_default=False,
        ),
    ]
