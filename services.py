def convert_currency(amount, cur):
    if cur.lower() == 'usd':
        return round(amount * 89.5)
    elif cur.lower() == 'eur':
        return round(amount * 96)
