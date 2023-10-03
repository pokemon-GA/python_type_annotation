price: int = 100
tax: float = 1.1

def calc(price: int, tax: float) -> int:
    result = price * tax
    return int(result)

print(calc(price, tax))