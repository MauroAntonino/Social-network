# Generated by Django 2.0.7 on 2020-05-14 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('apelidio', models.CharField(max_length=30)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos/')),
            ],
        ),
    ]
