# Generated by Django 2.1.2 on 2018-11-03 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0014_auto_20181103_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='show',
            name='days',
            field=models.ManyToManyField(to='shows.Days'),
        ),
    ]
