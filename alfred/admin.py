from django.contrib import admin

from alfred.models import MyBook, Checkpoint, WishList

admin.site.register(MyBook)
admin.site.register(Checkpoint)
admin.site.register(WishList)
