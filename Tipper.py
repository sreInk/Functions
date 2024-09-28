def tc(bl,tx):
    total = bl*(1 + 0.01*tx)
    total = round(total,2)
    print(f"Please Pay ${total}")

tc(150,20)
    