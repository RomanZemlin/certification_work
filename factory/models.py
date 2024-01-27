from django.db import models


class Factory(models.Model):
    # Модель завода
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"

    def __str__(self):
        return self.name


class RetailNetwork(models.Model):
    # Модель розничной сети
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    parent = models.ForeignKey(Factory, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Розничная сеть"
        verbose_name_plural = "Розничные сети"

    def __str__(self):
        return self.name


class IndividualEntrepreneur(models.Model):
    # Модель индивидуального предпринимателя
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    parent = models.ForeignKey(RetailNetwork, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"

    def __str__(self):
        return self.name


class Product(models.Model):
    # Модель продукта
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    release_date = models.DateField()
    supplier = models.ForeignKey(IndividualEntrepreneur, on_delete=models.CASCADE)
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name
