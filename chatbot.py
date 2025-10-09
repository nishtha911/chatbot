#basic idea

def get_chatbot_response(user_input):
    user_input_lower = user_input.lower()

    if "hello" in user_input_lower or "hi" in user_input_lower or "hey" in user_input_lower:
        return "Hello! I am a virtual assistant for MyOnlineStore. How can I help you today? You can ask me about orders, shipping, or returns."
    
    elif "order status" in user_input_lower or "where is my order" in user_input_lower or "track my order" in user_input_lower:
        return "I can help with that. Please provide your order number so I can check its status for you."
    
    elif "shipping" in user_input_lower or "delivery" in user_input_lower or "how long" in user_input_lower:
        return "Our standard shipping takes 3-5 business days. For more detailed information, please visit our Shipping Policy page on our website."
        
    elif "return" in user_input_lower or "refund" in user_input_lower or "exchange" in user_input_lower:
        return "You can return unused items within 30 days for a full refund or exchange. Please visit our Returns Portal to start the process."
        
    elif "talk to human" in user_input_lower or "speak to a person" in user_input_lower or "agent" in user_input_lower:
        return "I am connecting you with a human agent now. Please be patient, and an agent will be with you shortly."

    elif user_input_lower.isdigit() and len(user_input_lower) == 5:
        order_number = user_input_lower
        return f"Thank you. Your order #{order_number} is currently 'In Transit' and is estimated to arrive in 2-3 business days. You can also check your email for a tracking link."
        
    
    else:
        return "I'm sorry, I don't understand that request. Can you please rephrase your question or ask about a different topic? (e.g., 'shipping', 'returns', 'order status')."

if __name__ == "__main__":
    print("Welcome to the MyOnlineStore Chatbot! (Type 'exit' to quit)")
    while True:
        user_input = input("👤: ")
        if user_input.lower() == "exit":
            print("🤖: Goodbye!")
            break
        
        response = get_chatbot_response(user_input)
        print(f"🤖: {response}")