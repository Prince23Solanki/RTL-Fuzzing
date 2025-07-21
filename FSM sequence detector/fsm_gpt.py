from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import re
import random

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

prompt = """Generate 2-bit binary test inputs for FSM sequence detector (1011).
Each line = reset, din
Examples:
00
01
11
"""

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(
    **inputs,
    max_length=100,
    do_sample=True,
    temperature=0.7,
    top_k=40,
    num_return_sequences=1
)

text = tokenizer.decode(outputs[0], skip_special_tokens=True)
binary_lines = re.findall(r"[01]{2}", text)

if len(binary_lines) < 10:
    print("⚠️ GPT2 didn't generate enough. Using fallback.")
    binary_lines = []
    for _ in range(10):
        reset = format(random.randint(0, 1), '01b')
        din = format(random.randint(0, 1), '01b')
        binary_lines.append(reset + din)

with open("FSM/inputs.txt", "w") as f:
    for line in binary_lines[:10]:
        f.write(line + "\n")

print("✅ FSM inputs.txt generated.")
