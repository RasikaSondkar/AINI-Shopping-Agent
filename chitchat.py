def handle_chitchat(user_input):
    greetings = ["hi", "hello", "hey"]
    how_are_you = ["how are you"]
    thanks = ["thanks", "thank you"]

    if any(word in user_input for word in greetings):
        return "Hi 😊 I’m AINI. Tell me what product you'd like to compare."

    if any(word in user_input for word in how_are_you):
        return "I’m doing great! Ready to find you the best deal 🛒"

    if any(word in user_input for word in thanks):
        return "You're welcome! Happy to help 💛"

    return None
