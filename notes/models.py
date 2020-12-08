from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError

class NoteSubject(models.Model):
    notes_id=models.AutoField
    notes_teacher=models.CharField(max_length=50, default="")
    notes_subject = models.CharField(max_length=50, default="")
    notes_subinshort = models.CharField(max_length=50, default="")


    def __str__(self):
        return self.notes_subject


class DSDNotes(models.Model):
    notes_id = models.AutoField
    notes_name = models.CharField(max_length=50, default="")
    notes_sub = models.CharField(max_length=50, default="")
    notes_image = models.ImageField(upload_to="notes/images", null=True, blank=True)
    pub_date = models.DateTimeField(null=True)
    notes_document = models.FileField(upload_to="notes/images", null=True, blank=True)

    def __str__(self):
        return self.notes_name


class DAANotes(models.Model):
    notes_id = models.AutoField
    notes_name = models.CharField(max_length=50, default="")
    notes_sub = models.CharField(max_length=50, default="")
    notes_image = models.ImageField(upload_to="notes/images", null=True, blank=True)
    pub_date = models.DateTimeField(null=True)
    notes_document = models.FileField(upload_to="notes/images", null=True, blank=True)

    def __str__(self):
        return self.notes_name