from core.models import Page
from blocks.content_blocks import (
    benefits_block, ingredients_block, usage_block, safety_block, pricing_block
)

class ProductPageAgent:
    def build_page(self, product):
        return Page(
            page_type="product",
            content={
                "name": product.name,
                "concentration": product.concentration,
                "sections": {
                    "benefits": benefits_block(product),
                    "ingredients": ingredients_block(product),
                    "usage": usage_block(product),
                    "safety": safety_block(product),
                    "pricing": pricing_block(product)
                }
            }
        )
