from django.contrib import admin
from .import models

admin.site.register(models.Tags)
admin.site.register(models.Badge)
admin.site.register(models.UserProfile)
admin.site.register(models.ForumCategory)
admin.site.register(models.Vote)
admin.site.register(models.Topic)
admin.site.register(models.UserTopics)
admin.site.register(models.Comment)
admin.site.register(models.Timeline)
admin.site.register(models.Attachment)
admin.site.register(models.Facebook)
admin.site.register(models.Google)
admin.site.register(models.Twitter)