from transformers import pipeline

def main():
    # Initialize the LLM pipeline
    generator = pipeline('text-generation', model='gpt-3.5-turbo')

    while True:
        # Get user input
        user_input = input("Ask a question: ")

        if user_input.lower() in ['exit', 'quit']:
            break

        # Generate response
        response = generator(user_input, max_length=100, num_return_sequences=1)
        print("Response:", response[0]['generated_text'])

if __name__ == "__main__":
    main()
