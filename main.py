import os
import openai
openai.api_key = os.getenv("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")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
