from core.models import Page
from blocks.content_blocks import faq_items

class FAQPageAgent:
    def build_page(self, product, questions):
        return Page(
            page_type="faq",
            content={
                "title": "Frequently Asked Questions",
                "faqs": faq_items(product, questions)
            }
        )
