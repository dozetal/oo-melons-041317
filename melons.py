"""

Classes for melon orders.

"""


# Establish Super Class AbstractMelonOrder
class AbstractMelonOrder(object):
    """ A melon order from ______."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = 0
        # self.order_type = "abstract"

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
    def __init__(self, order_type):
        super(DomesticMelonOrder, self).__init__(order_type, "domestic")

        self.tax = 0.08

    """Initialize melon order attributes."""


# Establish sub-class InternationalMelonOrder
class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    # Default for international orders
    def __init__(self, order_type):
        super(InternationalMelonOrder, self).__init__(order_type, "international")

        self.country_code = country_code
        self.tax = 0.17

    """Initialize melon order attributes."""

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

# Code Review by Ahamd # ZOMG AWESOME!!!!!!
