# Generated by Django 4.2.5 on 2024-01-04 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('time', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Experiences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=40)),
                ('number', models.CharField(blank=True, max_length=20)),
                ('url', models.URLField(blank=True, max_length=100)),
                ('linkedin', models.CharField(blank=True, max_length=50)),
                ('github', models.CharField(blank=True, max_length=50)),
                ('twitter', models.CharField(blank=True, max_length=50)),
                ('career_profile', models.TextField(blank=True, max_length=1000)),
                ('roles', models.JSONField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/')),
                ('companies', models.ManyToManyField(blank=True, to='mainapp.companies')),
                ('education', models.ManyToManyField(blank=True, to='mainapp.education')),
                ('experiences', models.ManyToManyField(blank=True, to='mainapp.experiences')),
                ('interests', models.ManyToManyField(blank=True, to='mainapp.interests')),
                ('languages', models.ManyToManyField(blank=True, to='mainapp.languages')),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.profession')),
            ],
        ),
        migrations.AddField(
            model_name='education',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.school'),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cities', to='mainapp.country')),
            ],
        ),
    ]
