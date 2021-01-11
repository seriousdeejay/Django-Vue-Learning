# Generated by Django 3.1.5 on 2021-01-10 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(max_length=255)),
                ('parent_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lists.list')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
