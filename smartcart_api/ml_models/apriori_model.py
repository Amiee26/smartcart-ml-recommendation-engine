import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Load dataset once
data = pd.read_csv("/var/www/html/smartcart/dataset/groceries.csv")

# Convert to basket format
basket = data.groupby(['Member_number', 'itemDescription'])['itemDescription'] \
        .count().unstack().fillna(0)

basket = basket.map(lambda x: True if x > 0 else False)

# Train Apriori model once
frequent_items = apriori(basket, min_support=0.01, use_colnames=True)

rules = association_rules(frequent_items, metric="lift", min_threshold=1)

def generate_recommendations(product_name):

    recommendations = []

    for index, row in rules.iterrows():

        antecedents = list(row['antecedents'])
        consequents = list(row['consequents'])

        for item in antecedents:
            if product_name.lower() in item.lower():
                recommendations.extend(consequents)

    return list(set(recommendations))
