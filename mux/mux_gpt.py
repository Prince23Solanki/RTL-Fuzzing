from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import re
import random

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

prompt = """Generate 6-bit binary inputs for a 4-to-1 multiplexer (MUX).
Each line = sel[1:0] + din[3:0]
Examples:
001011
110101
101100
"""

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(
    **inputs,
    max_length=150,
    do_sample=True,
    top_k=40,
    temperature=0.7,
    num_return_sequences=1
)

text = tokenizer.decode(outputs[0], skip_special_tokens=True)
binary_lines = re.findall(r"[01]{6}", text)

# fallback if not enough valid lines
if len(binary_lines) < 10:
    print("⚠️ GPT2 didn't generate enough binary lines. Using fallback.")
    binary_lines = []
    for _ in range(10):
        sel = format(random.randint(0, 3), '02b')
        din = format(random.randint(0, 15), '04b')
        binary_lines.append(sel + din)

# Save to mux/inputs.txt
with open("Mux/inputs.txt", "w") as f:
    for line in binary_lines[:10]:
        f.write(line + "\n")

print("✅ inputs.txt for MUX generated.")
