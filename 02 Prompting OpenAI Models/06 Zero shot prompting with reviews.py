client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define a multi-line prompt to classify sentiment
prompt = """Claddify sentiment of the statement using numbers 1 to 5, 1 being positive and 5 being negative:
1. Unbelievably good!
2. Shoes fell apart on the second use.
3. The shoes look nice, but they aren't very comfortable.
4. Can't wait to show them off!"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}],
  max_completion_tokens=100
)

print(response.choices[0].message.content)
