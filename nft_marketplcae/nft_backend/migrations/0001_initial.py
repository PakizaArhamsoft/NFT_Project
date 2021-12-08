# Generated by Django 4.0 on 2021-12-08 13:44

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('image', models.TextField(null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_removed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CollectedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('logo_image', models.ImageField(blank=True, upload_to='')),
                ('featured_image', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField(null=True)),
                ('url', models.TextField(null=True)),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('is_removed', models.BooleanField(default=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_category', to='nft_backend.category')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('profile_image', models.ImageField(blank=True, upload_to='')),
                ('is_verified', models.BooleanField(default=False)),
                ('facebook', models.TextField(null=True)),
                ('tweeter', models.TextField(null=True)),
                ('linked_in', models.TextField(null=True)),
                ('is_removed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField(null=True)),
                ('price', models.FloatField(null=True)),
                ('royality', models.FloatField(null=True)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('sale_type', models.CharField(choices=[('is_put_on_sale', 'Is Put On Sale'), ('is_instant_sale_price', 'Is Instant Sale Price'), ('is_unlock_purchase', 'Is Unlock Purchase')], max_length=40)),
                ('is_removed', models.BooleanField(default=False)),
                ('total_views', models.IntegerField(default=0)),
                ('collection_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_collection', to='nft_backend.collection')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_user', to='nft_backend.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_balance', models.FloatField(null=True)),
                ('wallet_address', models.TextField(null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to='nft_backend.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='WalletTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(null=True)),
                ('transaction_type', models.TextField(null=True)),
                ('transaction_date', models.DateTimeField(auto_now=True)),
                ('wallet_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wallet_transaction', to='nft_backend.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='PriceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(null=True)),
                ('item_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_history', to='nft_backend.item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold_price', models.FloatField(null=True)),
                ('sold_date', models.DateTimeField(auto_now=True)),
                ('service_fee', models.FloatField(null=True)),
                ('buyer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_buyer', to='nft_backend.customuser')),
                ('collected_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_transaction', to='nft_backend.collecteditem')),
                ('wallet_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_wallet', to='nft_backend.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='FavouriteItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favourite_item', to='nft_backend.item')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_favourite', to='nft_backend.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.TextField(null=True)),
                ('resolved_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='FAQ_user', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('subject', models.TextField(null=True)),
                ('message', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('is_responded', models.BooleanField(default=False)),
                ('resolved_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resolved_user', to='auth.user')),
            ],
        ),
        migrations.AddField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to='nft_backend.customuser'),
        ),
        migrations.AddField(
            model_name='collecteditem',
            name='item_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collected_item', to='nft_backend.item'),
        ),
        migrations.AddField(
            model_name='collecteditem',
            name='owner_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_owner', to='nft_backend.customuser'),
        ),
        migrations.CreateModel(
            name='Biding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biding_date', models.DateTimeField(auto_now=True)),
                ('price', models.FloatField(null=True)),
                ('expiry_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('currency_type', models.TextField(null=True)),
                ('item_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='biding_item', to='nft_backend.item')),
                ('offer_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_biding', to='nft_backend.customuser')),
            ],
        ),
    ]
