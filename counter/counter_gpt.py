from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import re
import random

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

# Prompt for 3-bit inputs (clk is auto toggled in TB, we care about reset and up_down)
prompt = """Generate binary inputs for Verilog counter: 3-bit (reset + up_down control).
Examples:
001
100
111
010
"""

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(
    **inputs,
    max_length=150,
    do_sample=True,
    top_k=50,
    temperature=0.7,
    num_return_sequences=1
)

text = tokenizer.decode(outputs[0], skip_special_tokens=True)
binary_lines = re.findall(r"[01]{3}", text)

if len(binary_lines) < 10:
    print("⚠️ GPT2 didn't generate enough lines. Using fallback.")
    binary_lines = []
    for _ in range(10):
        clk = '0'  # Ignored, so hardcoded
        reset = format(random.randint(0, 1), '01b')
        up_down = format(random.randint(0, 1), '01b')
        binary_lines.append(clk + reset + up_down)

# Save to counter/inputs.txt
with open("counter/inputs.txt", "w") as f:
    for line in binary_lines[:10]:
        f.write(line + "\n")

print("✅ Counter inputs.txt generated.")
