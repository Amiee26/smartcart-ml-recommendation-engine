import pandas as pd
from apriori_model import generate_recommendations

data = pd.read_csv("../dataset/transactions.csv")

rules = generate_recommendations(data)

print(rules[['antecedents','consequents','support','confidence','lift']])
