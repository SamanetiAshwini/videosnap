from django.db.models import CharField
from accounts.views import about
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    about=CharField(max_length=500)
    city=models.TextField()
    distict=models.TextField()
    state=models.TextField()
    profile_picture=models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Achievements(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.user.username

class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.user.username

class Certifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certificate_name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

class Languages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Interests(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

class SocialLinks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.user.username

class Awards(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    award_name = models.CharField(max_length=200)
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username