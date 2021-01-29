from django.db import models


# Class for every plain text object
class CommonText(models.Model):
    id = models.CharField(max_length=100, primary_key=True)     # id = 'menu_start'

    def __str__(self):
        return f"{self.id}"


class CommonTextTrans(models.Model):
    lang = models.CharField(max_length=8)   # lang = 'en'
    translation = models.TextField()        # translation = 'Start'
    parent_id = models.ForeignKey(CommonText, on_delete=models.CASCADE)  # parent_id = 'menu_start'

    def __str__(self):
        return f"lang:{self.lang} for {self.parent_id}"


class ServicesItem(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.id


class ServicesItemTrans(models.Model):
    lang = models.CharField(max_length=8)
    # <b>Headline<b>
    headline = models.CharField(max_length=200)
    # Text
    content = models.TextField()
    parent_id = models.ForeignKey(ServicesItem, on_delete=models.CASCADE)


class WorkflowItem(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.id


class WorkflowItemTrans(models.Model):
    lang = models.CharField(max_length=8)
    title = models.CharField(max_length=100)
    point01 = models.CharField(max_length=200)
    point02 = models.CharField(max_length=200, blank=True)
    point03 = models.CharField(max_length=200, blank=True)
    point04 = models.CharField(max_length=200, blank=True)
    point05 = models.CharField(max_length=200, blank=True)
    workf_item = models.ForeignKey(WorkflowItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"1){self.point01}, 2){self.point02}, 3){self.point03}, 4){self.point04}, 5){self.point05}"


# Class for adding a team member
class TeamMember(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(default='default.jpg', upload_to='team_avatars')

    def __str__(self):
        return self.name


class TeamMemberTrans(models.Model):
    lang = models.CharField(max_length=8)
    role = models.CharField(max_length=30)
    description = models.TextField()
    team_member = models.ForeignKey(TeamMember, on_delete=models.CASCADE)

    def __str__(self):
        return f"lang:{self.lang} for {self.team_member.name}, role:{self.role}"


# Class for adding clients' logos
class ClientLogo(models.Model):
    name = models.CharField(max_length=50, default='client_name')
    image = models.ImageField(upload_to='client_logos')

    def __str__(self):
        return f"logo of {self.name}"

