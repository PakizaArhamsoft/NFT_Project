from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class CustomUser(User):
    profile_image = models.ImageField(blank=True)
    is_verified = models.BooleanField(default=False)
    facebook = models.TextField(null=True)
    tweeter = models.TextField(null=True)
    linked_in = models.TextField(null=True)
    is_removed = models.BooleanField(default=False)


class Category(models.Model):
    name = models.TextField(null=True)
    image = models.TextField(null=True)
    is_active = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)


class Collection(models.Model):
    name = models.TextField(null=True)
    logo_image = models.ImageField(blank=True)
    featured_image = models.ImageField(blank=True)
    description = models.TextField(null=True)
    url = models.TextField(null=True)
    creation_date = models.DateTimeField(auto_now=True)
    is_removed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, related_name="item_category", on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(CustomUser, related_name="profile_user", on_delete=models.CASCADE, null=True)


class Item(models.Model):
    name = models.TextField(null=True)
    image = models.ImageField(blank=True)
    description = models.TextField(null=True)
    price = models.FloatField(null=True)
    royality = models.FloatField(null=True)
    created_date = models.DateTimeField(auto_now=True)
    choices = [
        ("is_put_on_sale", "Is Put On Sale"),
        ("is_instant_sale_price", "Is Instant Sale Price"),
        ("is_unlock_purchase", "Is Unlock Purchase")
    ]
    sale_type = models.CharField(max_length=40, choices=choices)
    is_removed = models.BooleanField(default=False)
    collection_id = models.ForeignKey(Collection, related_name="item_collection", on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(CustomUser, related_name="item_user", on_delete=models.CASCADE, null=True)
    total_views = models.IntegerField(default=0)


class FavouriteItem(models.Model):
    user_id = models.ForeignKey(CustomUser, related_name="user_favourite", on_delete=models.CASCADE, null=True)
    item_id = models.ForeignKey(Item, related_name="favourite_item", on_delete=models.CASCADE, null=True)


class CollectedItem(models.Model):
    owner_id = models.ForeignKey(CustomUser, related_name="item_owner", on_delete=models.CASCADE, null=True)
    item_id = models.ForeignKey(Item, related_name="collected_item", on_delete=models.CASCADE, null=True)


class Wallet(models.Model):
    user = models.ForeignKey(CustomUser, related_name="wallet", on_delete=models.CASCADE, null=True)
    current_balance = models.FloatField(null=True)
    wallet_address = models.TextField(null=True)
    is_active = models.BooleanField(default=False)


class ItemTransaction(models.Model):
    buyer_id = models.ForeignKey(CustomUser, related_name="item_buyer", on_delete=models.CASCADE, null=True)
    collected_item = models.ForeignKey(CollectedItem, related_name="item_transaction", on_delete=models.CASCADE,
                                       null=True)
    sold_price = models.FloatField(null=True)
    sold_date = models.DateTimeField(auto_now=True)
    wallet_id = models.OneToOneField(Wallet, related_name="user_wallet", on_delete=models.CASCADE, null=True)
    service_fee = models.FloatField(null=True)


class PriceHistory(models.Model):
    item_id = models.ForeignKey(Item, related_name="item_history", on_delete=models.CASCADE, null=True)
    price = models.FloatField(null=True)


class WalletTransaction(models.Model):
    wallet_id = models.OneToOneField(Wallet, related_name="wallet_transaction", on_delete=models.CASCADE, null=True)
    amount = models.FloatField(null=True)
    transaction_type = models.TextField(null=True)
    transaction_date = models.DateTimeField(auto_now=True)


class Biding(models.Model):
    offer_by = models.ForeignKey(CustomUser, related_name="user_biding", on_delete=models.CASCADE, null=True)
    biding_date = models.DateTimeField(auto_now=True)
    price = models.FloatField(null=True)
    expiry_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    item_id = models.ForeignKey(Item, related_name="biding_item", on_delete=models.CASCADE, null=True)
    currency_type = models.TextField(null=True)


class Contact(models.Model):
    name = models.TextField(null=True)
    email = models.EmailField(null=True)
    subject = models.TextField(null=True)
    message = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)
    is_responded = models.BooleanField(default=False)
    # field issue resolved by staff member
    resolved_by = models.ForeignKey(User, related_name="resolved_user", on_delete=models.CASCADE, null=True)


class FAQ(models.Model):
    title = models.TextField(null=True)
    description = models.TextField(null=True)
    last_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    category = models.TextField(null=True)
    # field issue resolved by staff member
    resolved_by = models.ForeignKey(User, related_name="FAQ_user", on_delete=models.CASCADE, null=True)

