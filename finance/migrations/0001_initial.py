# Generated by Django 2.1.7 on 2019-05-29 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reception', '0001_initial'),
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charges', models.CharField(default=0, max_length=200)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reception.Patient')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.Treatment')),
            ],
        ),
    ]