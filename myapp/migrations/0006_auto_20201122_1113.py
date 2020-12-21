# Generated by Django 3.1.2 on 2020-11-22 16:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20201018_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(0, 'Cancelled'), (1, 'Confirmed'), (2, 'On Hold')], default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='myapp.student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='student',
            name='province',
            field=models.CharField(default='ON', max_length=2),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer', models.EmailField(max_length=254)),
                ('rating', models.PositiveIntegerField()),
                ('comments', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.course')),
            ],
        ),
    ]
