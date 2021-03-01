# Another project management software
# Copyright (C) 2021 Salah OSFOR <osfor.salah@gmail.com>

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator


class Team(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    name_clean = models.CharField(max_length=100, editable=False)
    description = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_clean = str(self.name).lower().strip()
        super(Team).save(*args, **kwargs)


class SkillField(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    name_clean = models.CharField(max_length=100, editable=False)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_clean = str(self.name).lower().strip()
        super(SkillField).save(*args, **kwargs)


class Skill(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    name_clean = models.CharField(max_length=100, editable=False)
    field = models.ForeignKey(SkillField, null=False, blank=False, on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_clean = str(self.name).lower().strip()
        super(Skill).save(*args, **kwargs)


class Member(User):
    manager = models.ForeignKey("self", null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.username


class MemberSkill(models.Model):
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.PROTECT)
    skill = models.ForeignKey(Skill, null=False, blank=False, on_delete=models.PROTECT)
    proficiency = models.IntegerField(null=False, blank=False, validators=[
        MinValueValidator(0), MaxValueValidator(10)
    ])
    appraiser = models.IntegerField(null=False, blank=False, choices=(
        (1, 'SELF'),
        (2, 'MANAGER'),
        (3, 'AUTOMATED')
    ))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.member.__str__() + ':' + self.skill.__str__()

    class Meta:
        unique_together = [['member', 'skill', 'appraiser']]
