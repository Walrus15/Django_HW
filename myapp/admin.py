from django.contrib import admin

from .models import  Author, Book, \
    Author_two, User_two, Book_two, \
    Likes, Comments, Articles, Comment_coms

admin.site.register(Author)
admin.site.register(Book)

admin.site.register(Author_two)
admin.site.register(User_two)
admin.site.register(Book_two)

admin.site.register(Likes)
admin.site.register(Comment_coms)
admin.site.register(Comments)
admin.site.register(Articles)



