from django.db import models

class ProjectIdea(models.Model):
    BRANCH_CHOICES = [
        ('CSE', 'Computer Science'),
        ('ECE', 'Electronics'),
        ('EEE', 'Electrical'),

        ('ME', 'Mechanical'),
        ('CE', 'Civil'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(default="noemail@example.com", blank=True, null=True)
    college = models.CharField(max_length=150)
    branch = models.CharField(max_length=10, choices=BRANCH_CHOICES)
    domain = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.domain}"

from django.db import models

class ProjectRequest(models.Model):
    BRANCH_CHOICES = [
        ('CSE', 'Computer Science'),
        ('ECE', 'Electronics'),
        ('EEE', 'Electrical'),
        ('ME', 'Mechanical'),
        ('CE', 'Civil'),
    ]

    DOMAIN_CHOICES = [
        ('Web Development', 'Web Development'),
        ('Machine Learning', 'Machine Learning'),
        ('AI', 'AI'),
        ('Cloud Computing', 'Cloud Computing'),
        ('', 'Not Specified'),
    ]

    name = models.CharField(max_length=100)
    college = models.CharField(max_length=150)
    branch = models.CharField(max_length=10, choices=BRANCH_CHOICES)
    domain = models.CharField(max_length=50, choices=DOMAIN_CHOICES, blank=True)
    email = models.EmailField(default="noemail@example.com")
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.domain if self.domain else 'Not Specified'}"
