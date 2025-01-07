# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Chapter(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    work_id = models.TextField(blank=True, null=True)
    section_number = models.BigIntegerField(blank=True, null=True)
    chapter_number = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chapter'


class Character(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    id = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    abbrev = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    speech_count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'character'


class CharacterWork(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    character_id = models.TextField(blank=True, null=True)
    work_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'character_work'


class Paragraph(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    work_id = models.TextField(blank=True, null=True)
    paragraph_num = models.BigIntegerField(blank=True, null=True)
    character_id = models.TextField(blank=True, null=True)
    plain_text = models.TextField(blank=True, null=True)
    phonetic_text = models.TextField(blank=True, null=True)
    stem_text = models.TextField(blank=True, null=True)
    paragraph_type = models.TextField(blank=True, null=True)
    section_number = models.BigIntegerField(blank=True, null=True)
    chapter_number = models.BigIntegerField(blank=True, null=True)
    char_count = models.BigIntegerField(blank=True, null=True)
    word_count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paragraph'


class Wordform(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    plain_text = models.TextField(blank=True, null=True)
    phonetic_text = models.TextField(blank=True, null=True)
    stem_text = models.TextField(blank=True, null=True)
    occurences = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wordform'


class Work(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    id = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    long_title = models.TextField(blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)
    genre_type = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    total_words = models.BigIntegerField(blank=True, null=True)
    total_paragraphs = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work'
