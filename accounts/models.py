from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# User 계정을 커스텀 마이징 시키는 방법은 4가지 정도의 방법이 있다
# 1) proxy 활용
# 2) AbstractUser 상속 하는 방법
# 3) AbstractBaseUser 상속 하는 방법
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", "남성"
        FEMALE = "F", "여성"

    gender = models.CharField(
        verbose_name="성별", max_length=1, choices=GenderChoices.choices
    )
