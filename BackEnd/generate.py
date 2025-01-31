import os
import openai

# Ensure chemical_names.txt exists
if not os.path.exists("chemical_names.txt"):
    print("Error: chemical_names.txt not found")
    exit(1)

# Read extracted chemical names
with open("chemical_names.txt", "r") as f:
    chemical_names = f.read().strip()

if not chemical_names:
    print("Error: No chemical names found in chemical_names.txt")
    exit(1)

# OpenAI API Key (set your API key here)
openai.api_key = "your_openai_api_key"

# Define the prompt
prompt = f"Provide a detailed analysis of the following skincare ingredients: {chemical_names}. Mention their benefits and possible side effects."

# Call OpenAI API
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a skincare ingredient analysis expert."},
                  {"role": "user", "content": prompt}]
    )
    analysis_result = response["choices"][0]["message"]["content"].strip()

except Exception as e:
    analysis_result = f"Error in generating analysis: {str(e)}"

# Write the output to ans.txt
with open("ans.txt", "w") as ans_file:
    ans_file.write(analysis_result)

print("ans.txt generated successfully")
