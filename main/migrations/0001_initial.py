# Generated by Django 3.2.13 on 2022-11-30 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('description', models.TextField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog_About_Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryForTruck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cars', models.CharField(max_length=50)),
                ('isactive', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('from_somewhere', models.CharField(max_length=100)),
                ('to_somewhere', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField(default=True)),
                ('status', models.IntegerField(choices=[(0, 'NEW'), (1, 'PROCEED'), (2, 'DISMISS'), (3, 'COMPLETED')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Cost_Of_Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('shipping_cost', models.CharField(max_length=75)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-country'],
            },
        ),
        migrations.CreateModel(
            name='Delivery_Method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('shipping_cost', models.CharField(max_length=75)),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Delivery_Method_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('shipping_cost', models.CharField(max_length=75)),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='LengthCargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModeCargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Our_Services_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='image/serviceimages')),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TypeCargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='WeightCargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work_Principles_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='image/aboutimages')),
                ('is_active', models.BooleanField(default=True)),
                ('about', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.about_company')),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('image', models.ImageField(null=True, upload_to='image/truck_images')),
                ('description', models.TextField(max_length=50)),
                ('car_weight', models.FloatField(default=0)),
                ('car_length', models.FloatField(default=0)),
                ('is_active', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.categoryfortruck')),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('from_here', models.CharField(max_length=50)),
                ('to_here', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='apps/order/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='apps/order/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='apps/order/')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.truck')),
                ('mode_cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.modecargo')),
                ('type_cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.typecargo')),
                ('volume_cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.lengthcargo')),
                ('weight_cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.weightcargo')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='image/blogimages')),
                ('description', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.blog_about_truck')),
            ],
        ),
        migrations.CreateModel(
            name='About_Company_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='image/aboutimages')),
                ('is_active', models.BooleanField(default=True)),
                ('about', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.about_company')),
            ],
        ),
    ]
