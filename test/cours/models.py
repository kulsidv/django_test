from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
    title = models.CharField("Заголовок", max_length=256)
    description = models.TextField("Описание")
    created_at = models.DateTimeField("Добавлено", auto_now_add=True)

    class Meta:
        abstract = True


class Cours(BaseModel):
    start_date = models.DateField("Дата начала курса", default=None)
    end_date = models.DateField("Дата окончания курса", default=None)
    logo = models.ImageField("Логотип курса", upload_to='images/')

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


class Lesson(BaseModel):
    text = models.TextField("Текст урока")
    cours = models.OneToOneField(
        "Cours",
        on_delete=models.CASCADE,
        null=False,
        verbose_name="Урок",
        related_name="cours"
    )

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.IntegerField("Рейтинг")
    comment = models.TextField("Комментарий")
    cours = models.ForeignKey(
        "Cours",
        on_delete=models.CASCADE,
        verbose_name="Ревью",
        related_name="cours_review"
    )

    class Meta:
        verbose_name = "ревью"
        verbose_name_plural = "Ревью"

    def __str__(self):
        return self.comment
