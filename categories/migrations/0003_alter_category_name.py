# Generated by Django 3.2.15 on 2022-08-24 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('entertainment', 'Entertainment'), ('events', 'Events'), ('in_depth', 'In-depth'), ('opinion', 'Opinion'), ('news', 'News')], default='news', max_length=55),
        ),
    ]