from aisuite import AISuite

def main():
    # Initialize the AISuite
    aisuite = AISuite()

    while True:
        # Get user input
        user_input = input("Ask a question: ")

        if user_input.lower() in ['exit', 'quit']:
            break

        # Generate response
        try:
            response = aisuite.generate_text(model_name='gpt-3.5-turbo', prompt=user_input, max_length=100, num_return_sequences=1)
            print("Response:", response[0]['generated_text'])
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()