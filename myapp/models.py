from django.db import models



class Author(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title




class Author_two(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class User_two(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Book_two(models.Model):
    title = models.CharField(max_length=120)
    author = models.ManyToManyField(Author_two)
    user = models.ManyToManyField(User_two)
    availability = models.BooleanField()

    def __str__(self):
        return self.title


class Likes(models.Model):
    like = models.BooleanField(blank=False)


class Comment_coms(models.Model):
    comment = models.TextField(max_length=360)


class Comments(models.Model):
    comment = models.TextField(max_length=360)
    like = models.OneToOneField(Likes, on_delete=models.CASCADE)
    com_com = models.OneToOneField(Comment_coms, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment


class Articles(models.Model):
    title = models.CharField(max_length=60)
    comment = models.OneToOneField(Comments, on_delete=models.CASCADE)
    like = models.OneToOneField(Likes, on_delete=models.CASCADE)

    def __str__(self):
        return self.title







