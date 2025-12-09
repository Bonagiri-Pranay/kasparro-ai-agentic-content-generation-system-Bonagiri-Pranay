import json
from pathlib import Path
from core.models import Product
from agents.product_parser_agent import ProductParserAgent
from agents.question_generation_agent import QuestionGenerationAgent
from agents.faq_page_agent import FAQPageAgent
from agents.product_page_agent import ProductPageAgent
from agents.comparison_page_agent import ComparisonPageAgent

BASE = Path(__file__).resolve().parent.parent

class Orchestrator:
    def __init__(self):
        self.parser = ProductParserAgent()
        self.q_agent = QuestionGenerationAgent()
        self.faq_agent = FAQPageAgent()
        self.product_agent = ProductPageAgent()
        self.compare_agent = ComparisonPageAgent()

    def load_product(self):
        with open(BASE / "data/product_input.json") as f:
            data = json.load(f)
        return self.parser.parse(data)

    def save(self, name, data):
        out = BASE / f"output/{name}.json"
        with open(out, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def run(self):
        product = self.load_product()
        questions = self.q_agent.generate_questions(product)

        faq = self.faq_agent.build_page(product, questions)
        prod = self.product_agent.build_page(product)
        comp = self.compare_agent.build_page(product)

        self.save("faq", faq.content)
        self.save("product_page", prod.content)
        self.save("comparison_page", comp.content)

if __name__ == "__main__":
    Orchestrator().run()
