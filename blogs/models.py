from django.db import models

class Blog(models.Model):
    blog_title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.CharField(max_length=255, unique=True, null=False, blank=False)
    short_desc = models.CharField(max_length=500, null=True, blank=True)
    long_desc = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    status = models.BooleanField(default=True)
    admin_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey("account.user", related_name='blog_user', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.id} - {self.blog_title}'