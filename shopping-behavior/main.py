from shopping_analysis.ingestion import load_data
from shopping_analysis.cleaning import clean_data
from shopping_analysis.analysis import (
    purchases_by_season,
    avg_spend_by_age_group,
    avg_spend_by_gender,
    purchases_by_item,
    avg_spend_by_payment,
    avg_spend_by_location
)
from shopping_analysis.output import print_results

df = load_data('data/raw/shopping.csv')
df = clean_data(df)

print_results('Purchases by Season', purchases_by_season(df))
print_results('Avg Spend by Age Group', avg_spend_by_age_group(df))
print_results('Avg Spend by Gender', avg_spend_by_gender(df))
print_results('Purchases by Item', purchases_by_item(df))
print_results('Avg Spend by Payment Method', avg_spend_by_payment(df))
print_results('Avg Spend by Location', avg_spend_by_location(df))