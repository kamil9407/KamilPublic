# Generated by Django 4.1.7 on 2023-07-11 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opinions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Przedmiot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opis', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='kategoria',
            name='nazwa',
            field=models.CharField(db_index=True, max_length=250),
        ),
    ]
