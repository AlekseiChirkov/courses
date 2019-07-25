from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    logo = models.TextField()

    def __str__(self):
        return str(self.name)

class Category(models.Model):
    name = models.CharField(max_length=64)
    imgpath = models.CharField(max_length=64)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)


class Branch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="branches")
    latitude = models.TextField()
    longitude = models.TextField()
    address = models.TextField()

    def __str__(self):
        return str(self.address)

class Contact(models.Model):
    phone = "PHONE"
    facebook = "FACEBOOK"
    email = "EMAIL"
    contact_choices = [
        (phone, "PHONE"),
        (facebook, "FACEBOOK"),
        (email, "EMAIL")
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="contacts")
    type = models.CharField(max_length=64, choices=contact_choices, default='')
    value = models.CharField(max_length=64, default='')

    def __str__(self):
        return str(self.type)
