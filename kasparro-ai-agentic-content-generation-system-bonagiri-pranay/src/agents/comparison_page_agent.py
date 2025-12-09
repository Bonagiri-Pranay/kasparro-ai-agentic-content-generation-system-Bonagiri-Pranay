from core.models import Page

class ComparisonPageAgent:
    def __init__(self):
        self.product_b = {
            "name": "RadiantShield Brightening Serum",
            "ingredients": ["Vitamin C", "Niacinamide"],
            "benefits": ["Brightening", "Supports even skin tone"],
            "price": "₹849"
        }

    def build_page(self, product):
        return Page(
            page_type="comparison",
            content={
                "product_a": {
                    "name": product.name,
                    "ingredients": product.key_ingredients,
                    "benefits": product.benefits,
                    "price": product.price
                },
                "product_b": self.product_b,
                "comparison": {
                    "ingredients": {
                        "A": product.key_ingredients,
                        "B": self.product_b["ingredients"]
                    },
                    "benefits": {
                        "A": product.benefits,
                        "B": self.product_b["benefits"]
                    },
                    "pricing": {
                        "A": product.price,
                        "B": self.product_b["price"]
                    }
                }
            }
        )
