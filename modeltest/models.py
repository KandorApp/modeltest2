from django.db import Models

class Post(models.Model):
    title = models.CharField(max_length=127)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING) # I don't want to die
    tag = models.OneToOneField(Tag, on_delete=models.CASCADE)
    body = models.TextField() # Markdown
    addenda = models.CharField(max_length=1023, null=True) # pretentious synonym for edit
    pub_date = models.DateTimeField("publication date")
    addenda_date = models.DateTimeField(null=True)
    deleted = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        #why delete if you can set the delete flag?
        if addenda == "coward":
            super(Post, self).delete(*args, **kwargs) # if you must
        else:
            self.deleted = True
            addenda += "Deleted attempted."
            self.save()
    class Meta:
        ordering = ['-pub_date']


class Author(models.Model):
    name = models.CharField("full name", max_length=63)
    email = models.EmailField()


    def __str__(self):
        return self.name

class Tag(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)
    note = models.CharField(max_length=255) # misc. message for future yusef
    tag1 = models.CharField("tag 1", max_length=31)
    tag2 = models.CharField("tag 2", max_length=31, null=True)
    tag3 = models.CharField("tag 3", max_length=31, null=True)


    def __str__(self):
        return self.post
