from django.db import models

# 1. Model Les Catégories
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nom de Catégorie")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return self.name

# 2. Model Les Produits
class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nom du Produit")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Catégorie")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix (DH)")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Quantité en Stock")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout")

    def __str__(self):
        return f"{self.name} ({self.quantity})"