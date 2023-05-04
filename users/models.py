# class User(models.Model):
#     login = models.CharField(max_length=100, null=True, verbose_name="Логин")
#     email = models.CharField(max_length=100, null=True, verbose_name="Электронная почта")
#     password = models.CharField(max_length=100, null=True, verbose_name="Пароль")
#     day_of_register = models.CharField(max_length=100, null=True, verbose_name="День рождения")
#     first_name = models.CharField(max_length=100, null=True, verbose_name="Фамилия")
#     last_name = models.CharField(max_length=100, null=True, verbose_name="Имя")
#     day_of_birthd = models.CharField(max_length=100, null=True, verbose_name="День рождения")


#     class Meta:
#         verbose_name = "Юзер"
#         verbose_name_plural = "Юзеры"

#     def __str__(self):
#         return f"{self.login}"
