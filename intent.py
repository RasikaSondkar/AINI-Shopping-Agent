import re

ELECTRONICS_KEYWORDS = {
    "laptop": ["laptop", "macbook", "notebook"],
    "smartphone": ["phone", "mobile", "iphone", "android"],
    "headphones": ["headphones", "earphones", "buds"],
    "smartwatch": ["watch", "smartwatch", "apple watch"]
}

def detect_products(user_input):
    detected = []
    user_input = user_input.lower()

    for product, keywords in ELECTRONICS_KEYWORDS.items():
        for word in keywords:
            if re.search(rf"\b{word}\b", user_input):
                detected.append(product)
                break

    return detected