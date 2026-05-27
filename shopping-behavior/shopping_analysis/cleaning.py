def clean_data(df):
    # Drop rows missing Age or Location
    df = df.dropna(subset=['Age', 'Location'])
    # Fill missing Review Rating with median
    df['Review Rating'] = df['Review Rating'].fillna(df['Review Rating'].median())
    return df