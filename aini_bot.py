from data import PRODUCT_DATA
from chitchat import handle_chitchat
from memory import Memory
from score import calculate_best_site

EXIT_WORDS = ["exit", "quit", "bye"]

memory = Memory()
awaiting_confirmation = False   # ✅ ADDED

print("🤖 Welcome to AINI - Smart Shopping Assistant")
print("I can compare: headphones, laptop, smartphone, smartwatch")
print("Type 'exit' anytime to quit.\n")

while True:
    try:
        user_input = input("You: ").lower().strip()

        # Exit
        if user_input in EXIT_WORDS:
            print("👋 AINI: Bye! Happy shopping 🛍️")
            break

        # ✅ YES / NO HANDLING (ADDED BLOCK)
        if awaiting_confirmation:
            if user_input in ["yes", "y"]:
                awaiting_confirmation = False
                print("🤖 AINI: Great! Tell me the product name.\n")
                continue

            elif user_input in ["no", "n"]:
                print("👋 AINI: Bye! Happy shopping 🛍️")
                break

            else:
                print("🤔 AINI: Please answer with yes or no.\n")
                continue

        # Handle empty/random input
        if len(user_input) < 2:
            print("🤔 AINI: Please enter something meaningful.\n")
            continue

        # Chitchat
        chat_response = handle_chitchat(user_input)
        if chat_response:
            print(f"AINI: {chat_response}\n")
            continue

        import re

        user_input = user_input.lower()

        # Remove special characters
        user_input = re.sub(r"[^\w\s]", "", user_input)

        # Detect product 
        product = None

        for item in PRODUCT_DATA:
         words = user_input.split()
         if item in words:
          product = item
          break

# If not found directly, check inside sentence
        if not product:
          for item in PRODUCT_DATA:
           if item in user_input:
            product = item
            break


        if not product:
            print("🤖 AINI: I currently support headphones, laptop, smartphone, and smartwatch.\n")
            continue

        memory.save("last_product", product)

        print("\n🔍 AINI: Comparing price, ratings & reviews...\n")

        results = PRODUCT_DATA[product]

        # Display comparison
        for site, data in results.items():
            print(f"{site.capitalize()} → ₹{data['price']} | ⭐ {data['rating']} | 📝 {data['reviews']} reviews")

        # Get best site using scorer module
        best_site = calculate_best_site(results)
        best = results[best_site]

        print("\n✅ AINI Recommendation:")
        print(f"Buy from {best_site.upper()}")
        print(f"Reason: Strong rating ({best['rating']}⭐), trusted by {best['reviews']} users, and competitive price ₹{best['price']}\n")

        print("💬 AINI: Would you like to compare another product? (yes/no)\n")
        awaiting_confirmation = True   # ✅ ADDED

    except Exception:
        print("⚠️ AINI: Something unexpected happened, but I’m still here 😊 Try again.\n")
        continue
