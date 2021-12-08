from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Item)
admin.site.register(ItemTransaction)
admin.site.register(Wallet)
admin.site.register(WalletTransaction)
admin.site.register(PriceHistory)
admin.site.register(FavouriteItem)
admin.site.register(FAQ)
admin.site.register(CollectedItem)
admin.site.register(Contact)
admin.site.register(Biding)
