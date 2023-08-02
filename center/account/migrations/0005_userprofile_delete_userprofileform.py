# Generated by Django 4.1.7 on 2023-07-26 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_userprofileform_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('lastname', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('zipcode', models.CharField(max_length=6, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='media/images/')),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfileForm',
        ),
    ]
