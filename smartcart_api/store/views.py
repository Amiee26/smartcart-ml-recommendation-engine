from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from ml_models.apriori_model import generate_recommendations


def home(request):
    return render(request, "index.html")


def recommend_products(request, product_name):

    recommendations = generate_recommendations(product_name)[:8]

    if len(recommendations) == 0:
        recommendations = ["whole milk", "yogurt", "rolls/buns", "butter"]

    return JsonResponse({
        "product": product_name,
        "recommendations": recommendations
    })


def suggest_products(request):

    query = request.GET.get('q', '').lower()

    data = pd.read_csv("/var/www/html/smartcart/dataset/groceries.csv")

    products = data['itemDescription'].unique()

    suggestions = [p for p in products if query in p.lower()][:5]

    return JsonResponse({"suggestions": suggestions})


def top_products(request):

    data = pd.read_csv("/var/www/html/smartcart/dataset/groceries.csv")

    top = data['itemDescription'].value_counts().head(10)

    return JsonResponse(top.to_dict())
