from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class Product:
    name: str
    concentration: str
    skin_type: List[str]
    key_ingredients: List[str]
    benefits: List[str]
    how_to_use: str
    side_effects: str
    price: str

@dataclass
class Question:
    text: str
    category: str

@dataclass
class Page:
    page_type: str
    content: Dict[str, Any]
