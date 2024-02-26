import openai

# Set up your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Define a function to interact with GPT-3
def ask_gpt3(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Get user input
user_input = input("Ask a financial question: ")

# Fetch financial data based on user_input (using a financial data API)

# Generate context-aware prompt
prompt = f"Given the current stock prices and market trends, {user_input}."
gpt3_response = ask_gpt3(prompt)

# Display GPT-3 response with financial data
print("Chatbot Response:", gpt3_response)
