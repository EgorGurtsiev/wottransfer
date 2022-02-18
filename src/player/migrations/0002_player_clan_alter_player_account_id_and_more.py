# Generated by Django 4.0.1 on 2022-01-31 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clan', '0001_initial'),
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='clan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player', to='clan.clan'),
        ),
        migrations.AlterField(
            model_name='player',
            name='account_id',
            field=models.CharField(max_length=8, primary_key=True, serialize=False, unique=True, verbose_name='ID в БД wargaming'),
        ),
        migrations.AlterField(
            model_name='player',
            name='expires_at',
            field=models.DateTimeField(verbose_name='Дата истечения токена'),
        ),
        migrations.AlterField(
            model_name='player',
            name='username',
            field=models.CharField(max_length=25, unique=True, verbose_name='Имя в игре'),
        ),
    ]
