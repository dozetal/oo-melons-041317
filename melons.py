"""

Classes for melon orders.

"""


# Establish Super Class AbstractMelonOrder
class AbstractMelonOrder(object):
    """ A melon order from ______."""

    def __init__(self, species, qty, tax, order_type):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax
        self.order_type = order_type

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


# Establish sub-class DomesticMelonOrder
class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    # Default for domestic orders
    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty, 0.08, "domestic")

    """Initialize melon order attributes."""


# Establish sub-class InternationalMelonOrder
class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    # Default for international orders
    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty, 0.17, "international")

        self.country_code = country_code


    """Initialize melon order attributes."""

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

# Code Review by Ahamd # ZOMG AWESOME!!!!!!
