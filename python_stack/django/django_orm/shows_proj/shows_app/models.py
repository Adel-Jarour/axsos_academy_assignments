from django.db import models
from datetime import date

# Create your models here.
class ShowManager(models.Manager):

    def validate(self, data, id=None):
        errors = {}

        title = data.get('title', '').strip()
        if not title:
            errors['title'] = "Title is required."
        elif Show.objects.filter(title=title).exclude(id=id).exists():
            errors['title'] = "Title must be unique."

        if not data.get('network', '').strip():
            errors['network'] = "Network is required."

        release_date_str = data.get('release_date', '').strip()
        if not release_date_str:
            errors['release_date'] = "Release date is required."
        else:
            try:
                release_date = date.fromisoformat(release_date_str)
                if release_date > date.today():
                    errors['release_date'] = "Release date cannot be in the future."
            except ValueError:
                errors['release_date'] = "Invalid date format."

        description = data.get('description', '').strip()
        if description and len(description) < 10:
            errors['description'] = "Description must be at least 10 characters long."

        return errors

    def create_show(self, data):
        errors = self.validate(data)
        if errors:
            return (None, errors)

        show = self.create(
            title=data.get('title', '').strip(),
            network=data.get('network', '').strip(),
            release_date=data.get('release_date'),
            description=data.get('description', '').strip()
        )
        return (show, None)

    def update_show(self, id, data):
        errors = self.validate(data, id=id)
        if errors:
            return (None, errors)

        show = self.get(id=id)
        show.title = data.get('title', '').strip()
        show.network = data.get('network', '').strip()
        show.release_date = data.get('release_date')
        show.description = data.get('description', '').strip()
        show.save()
        return (show, None)


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __str__(self):
        return f"{self.title} ({self.network}) - {self.release_date}"
