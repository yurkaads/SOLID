class Invoice:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items

    def calculate_total(self):
        return sum(item.price for item in self.items)


class InvoicePrinter:
    def print_invoice(self, invoice):
        print(f"Invoice for {invoice.customer}")
        for item in invoice.items:
            print(f"{item.name}: {item.price}")
        print(f"Total: {invoice.calculate_total()}")
