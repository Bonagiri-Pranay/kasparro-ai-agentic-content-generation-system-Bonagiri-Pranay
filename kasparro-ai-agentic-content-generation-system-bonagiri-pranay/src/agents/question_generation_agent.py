from core.models import Question

class QuestionGenerationAgent:
    def generate_questions(self, product):
        questions = [
            f"What is {product.name}?",
            "How do I use it?",
            "Is it safe for sensitive skin?",
            "What is the price?",
            "How does it compare to other serums?",
            "Can I use it daily?",
            "Will it brighten my skin?",
            "Can it help with dark spots?",
            "Is it suitable for oily skin?",
            "What are the key ingredients?",
            "Does it hydrate the skin?",
            "When should I apply it?",
            "Can I mix it with other skincare products?",
            "How long until I see results?",
            "Is it okay for combination skin?"
        ]
        categories = ["Informational", "Usage", "Safety", "Purchase", "Comparison"]
        return [Question(text=q, category=categories[i % 5]) for i, q in enumerate(questions)]
