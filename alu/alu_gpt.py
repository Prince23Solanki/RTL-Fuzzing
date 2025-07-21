from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import re

# Load GPT2
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

# Give sample binary inputs in the prompt
prompt = """Generate binary inputs (11-bit) for Verilog ALU testing.
Each line = A[3:0] B[3:0] opcode[2:0]
Examples:
10100011001
11010100100
00011111010
"""

#prompt = """Generate binary inputs (11-bit) for Verilog ALU testing.
#Each line = A[3:0] B[3:0] opcode[2:0]
#Make sure to include test cases with opcode = 101 and 110.

#Examples:
#01011010101
#11000111110
#00011111010
#"""


inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(
    **inputs,
    max_length=150,
    do_sample=True,
    top_k=40,
    temperature=0.7,
    num_return_sequences=1
)

# Decode and extract only 11-bit binary lines
text = tokenizer.decode(outputs[0], skip_special_tokens=True)
binary_lines = re.findall(r"\b[01]{11}\b", text)

# Safety check
if len(binary_lines) < 10:
    print("⚠️ GPT2 didn't generate enough binary lines. Using fallback.")
    import random
    binary_lines = []
    for _ in range(10):
        A = format(random.randint(0, 15), '04b')
        B = format(random.randint(0, 15), '04b')
        opcode = format(random.randint(0, 7), '03b')
        binary_lines.append(A + B + opcode)

# Save to inputs.txt
with open("alu/inputs.txt", "w") as f:
    for line in binary_lines[:10]:
        f.write(line + "\n")

print("✅ inputs.txt generated with", len(binary_lines[:10]), "lines.")

