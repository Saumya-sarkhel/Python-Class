
def converter(usd_val):
    inr_val = usd_val * 91
    print(usd_val, "USD =", inr_val, "INR")

usd_val = float(input("Enter the USD value: "))
converter(usd_val)
