import pandas as pd

def purchases_by_season(df):
    return df.groupby('Season')['Season'].count().sort_values(ascending=False)

def avg_spend_by_age_group(df):
    df['Age Group'] = pd.cut(df['Age'], bins=[0, 25, 35, 45, 55, 100],
                             labels=['18-25', '26-35', '36-45', '46-55', '55+'])
    return df.groupby('Age Group', observed=True)['Purchase Amount (USD)'].mean().round(2)

def avg_spend_by_gender(df):
    return df.groupby('Gender')['Purchase Amount (USD)'].mean().round(2)

def purchases_by_item(df):
    return df.groupby('Item Purchased')['Item Purchased'].count().sort_values(ascending=False)

def avg_spend_by_payment(df):
    return df.groupby('Payment Method')['Purchase Amount (USD)'].mean().round(2)

def avg_spend_by_location(df):
    return df.groupby('Location')['Purchase Amount (USD)'].mean().round(2).sort_values(ascending=False)