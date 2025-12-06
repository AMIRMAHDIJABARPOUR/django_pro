from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    category = models.ManyToManyField("Category", related_name="posts", blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def get_snippet(self):
        return self.content[:100] + "..." if len(self.content) > 100 else self.content

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        verbose_name = "Category"
        ordering = ("name",)

    def save(self, *args, **kwargs):
        if self.name:
            # generate slug from name only if slug is not set
            if not self.slug:
                base = slugify(self.name)
                slug = base
                i = 1
                # ensure uniqueness (exclude self when updating)
                while (
                    Category.objects.filter(slug=slug)
                    .exclude(pk=getattr(self, "pk", None))
                    .exists()
                ):
                    slug = f"{base}-{i}"
                    i += 1
                self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
