def create_item(name, qty, price):
    return {"name": name, "qty": qty, "price": price}

def calc_total(items):
    total = 0
    for item in items:
        total += item["qty"] * item["price"]
    return total

def format_invoice(customer, items):
    text = f"Customer: {customer}\n"
    text += "-" * 30 + "\n"
    for item in items:
        text += f"{item['name']} x {item['qty']} = {item['qty'] * item['price']}\n"
    text += "-" * 30 + "\n"
    text += f"Total: {calc_total(items)}"
    return text

def export_text(invoice_string):
    return invoice_string.split("\n")

items = [
    create_item("Pen", 2, 5.0),
    create_item("Notebook", 1, 15.0)
]

invoice = format_invoice("Nguyen Van A", items)
print(invoice)
print(export_text(invoice))
