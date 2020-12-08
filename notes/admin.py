from django.contrib import admin

from .models import NoteSubject, DSDNotes, DAANotes
admin.site.register(NoteSubject)
admin.site.register(DSDNotes)
admin.site.register(DAANotes)