from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import re
import random

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

prompt = """Generate 8-bit binary inputs for a priority encoder.
Each line = in[7:0]
Examples:
00000001
00000100
10000000
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
binary_lines = re.findall(r"[01]{8}", text)

if len(binary_lines) < 10:
    print("⚠️ GPT2 didn't generate enough. Using fallback.")
    binary_lines = []
    for _ in range(10):
        line = ''.join([random.choice('01') for _ in range(8)])
        binary_lines.append(line)

with open("priority_encoder/inputs.txt", "w") as f:
    for line in binary_lines[:10]:
        f.write(line + "\n")

print("✅ Encoder inputs.txt generated.")
