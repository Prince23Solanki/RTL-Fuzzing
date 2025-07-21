from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import re
import random

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

prompt = """Generate 4-bit binary inputs for Verilog D Flip-Flop test.
Each line = clk (auto), reset, enable, d
Examples:
0110
1011
0001
"""

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(
    **inputs,
    max_length=150,
    do_sample=True,
    temperature=0.7,
    top_k=50,
    num_return_sequences=1
)

text = tokenizer.decode(outputs[0], skip_special_tokens=True)
binary_lines = re.findall(r"[01]{4}", text)

if len(binary_lines) < 10:
    print("⚠️ GPT2 didn't generate enough valid lines. Using fallback.")
    binary_lines = []
    for _ in range(10):
        reset = format(random.randint(0, 1), '01b')
        enable = format(random.randint(0, 1), '01b')
        d = format(random.randint(0, 1), '01b')
        binary_lines.append('0' + reset + enable + d)  # '0' is placeholder clk

with open("dflipflop/inputs.txt", "w") as f:
    for line in binary_lines[:10]:
        f.write(line + "\n")

print("✅ DFF inputs.txt generated.")
