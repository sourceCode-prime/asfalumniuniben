# Generated by Django 3.2.6 on 2021-08-20 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0010_alter_profile_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bizhub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=300, unique=True)),
                ('business_sector', models.CharField(choices=[('Law', 'Law'), ('Software Development', 'Software Development'), ('Health Care', 'Health Care'), ('Accounting', 'Accounting'), ('Engineering', 'Engineering')], max_length=200)),
                ('description', models.TextField(help_text='Give a little description of your business')),
                ('locaton', models.TextField()),
                ('contact', models.CharField(max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profile')),
            ],
        ),
    ]
