client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a detailed prompt
prompt = """
Generate a product description for SonicPro headphones. Below are some features of these headphones:
- Active noise cancellation (ANC)
- 40-hour battery life
- Foldable design
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    # Experiment with max_completion_tokens and temperature settings
    max_completion_tokens=400,
    temperature=.2
)

print(response.choices[0].message.content)
