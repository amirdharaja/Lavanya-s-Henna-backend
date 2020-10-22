# Generated by Django 2.2.14 on 2020-10-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('henna', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='henna_area',
            field=models.CharField(choices=[('h', 'Hands'), ('f', 'Foots'), ('o', 'Others')], default='o', max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='package',
            field=models.CharField(choices=[('cb', 'Classic Bridal'), ('eb', 'Elegant Bridal'), ('rb', 'Royal Bridal'), ('wb1', 'Star Bridal 1'), ('wb2', 'Star Bridal 2')], default='cb', max_length=2, null=True),
        ),
    ]
