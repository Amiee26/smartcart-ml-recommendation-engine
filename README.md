# 🛒 SmartCart Recommendation System

## About the Project
This project is a simple implementation of a product recommendation system using Market Basket Analysis. The idea is to understand which products are frequently bought together and suggest related items to users.
For example, if a user searches for "milk", the system recommends products like bread or butter based on past transaction data.

## Why I Built This
I wanted to explore how real-world platforms like Amazon and Flipkart recommend products. This project helped me understand association rule mining and how data can be used to improve user experience.

## Features
- Search for a product and get related recommendations
- Auto-suggestion while typing (similar to e-commerce websites)
- Display of top-selling products
- Visual representation using charts

## Tech Stack
- Backend: Django (Python)
- Data Processing: Pandas, Mlxtend (Apriori Algorithm)
- Frontend: HTML, CSS, JavaScript
- Visualization: Chart.js
- Database: PostgreSQL

## Dataset
I used a groceries dataset (similar to datasets available on Kaggle) to simulate real-world transactions.

## How to Run the Project

```bash
cd smartcart_api
source ../venv/bin/activate
python manage.py runserver
