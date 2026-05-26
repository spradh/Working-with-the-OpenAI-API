client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": "Generate a catchy slogan for a fine-dining chinese restaurant"}],
  max_completion_tokens=100
)

print(response.choices[0].message.content)
