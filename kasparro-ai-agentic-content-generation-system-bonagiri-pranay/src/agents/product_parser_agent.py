from core.models import Product

class ProductParserAgent:
    def parse(self, raw):
        return Product(
            name=raw["name"],
            concentration=raw["concentration"],
            skin_type=raw["skin_type"],
            key_ingredients=raw["key_ingredients"],
            benefits=raw["benefits"],
            how_to_use=raw["how_to_use"],
            side_effects=raw["side_effects"],
            price=raw["price"]
        )
