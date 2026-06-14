from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Description(models.Model):
    content = models.TextField()
    course = models.OneToOneField(
        Course,
        on_delete=models.CASCADE,
        related_name='description'
    )

    def __str__(self):
        return f"Description for {self.course.name}"


class Comment(models.Model):
    content = models.TextField()
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.course.name}"
