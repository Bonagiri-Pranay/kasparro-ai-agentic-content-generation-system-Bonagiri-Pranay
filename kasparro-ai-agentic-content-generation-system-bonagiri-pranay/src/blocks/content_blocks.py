from core.models import Product, Question

# ---- Product Page Blocks ----

def benefits_block(product: Product):
    return {"headline": "Key Benefits", "items": product.benefits}

def ingredients_block(product: Product):
    return {"headline": "Key Ingredients", "items": product.key_ingredients}

def usage_block(product: Product):
    return {"headline": "How to Use", "instructions": product.how_to_use}

def safety_block(product: Product):
    return {"headline": "Safety", "details": product.side_effects}

def pricing_block(product: Product):
    return {"headline": "Price", "price": product.price, "currency": "INR"}

# ---- Rule-based FAQ Answer Generator ----

def answer_question(product: Product, q: Question):
    text = q.text.lower()

    if "what is" in text:
        return f"{product.name} is a {product.concentration} serum that helps with {', '.join(product.benefits)}."

    if "ingredient" in text:
        return f"It contains {', '.join(product.key_ingredients)}."

    if "skin" in text and ("type" in text or "good" in text or "suitable" in text):
        return f"It is suitable for {', '.join(product.skin_type)} skin types."

    if "use" in text or "apply" in text or "when should" in text:
        return product.how_to_use

    if "daily" in text or "every day" in text:
        return "Yes, you may use it daily if your skin tolerates it."

    if "result" in text or "how long" in text:
        return "Results usually require consistent use over a few weeks."

    if "safe" in text or "sensitive" in text:
        return f"May cause {product.side_effects} for sensitive skin. Patch testing is recommended."

    if "mix" in text or "combine" in text:
        return "Introduce it gradually and avoid combining too many strong actives."

    if "price" in text or "cost" in text:
        return f"The price is {product.price}."

    if "compare" in text:
        return "It focuses on Vitamin C brightening; other serums may vary in strength and support ingredients."

    return "This question relates to product usage based on the provided data."

def faq_items(product: Product, questions):
    return [
        {"question": q.text, "category": q.category, "answer": answer_question(product, q)}
        for q in questions
    ]
