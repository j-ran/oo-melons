"""Classes for melon orders."""

class AbstractMelonOrder():
    def __init__(self, species, qty, country_code = None):
        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
# order_type, tax, country_code

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

melon_order = DomesticMelonOrder("Crenshaw", 3)
melon_order_2 = InternationalMelonOrder("Crenshaw", 3, "AUS")