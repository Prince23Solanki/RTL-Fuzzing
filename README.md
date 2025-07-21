# 🔍 RTL Fuzzing for Enhanced Verification

This repository presents a structured RTL Fuzzing framework that uses GPT-2 to generate intelligent test inputs for verifying digital designs written in Verilog. The goal is to enhance functional coverage and detect corner-case bugs using AI-guided input generation.

---

## 📁 Folder Structure

Each design (ALU, MUX, Counter, D Flip-Flop, FSM, Priority Encoder) has its own folder with:

- `design.v` – RTL module  
- `*_tb.v` – Testbench that reads from inputs.txt  
- `*_gpt.py` – Python script to generate binary inputs using GPT-2  
- `inputs.txt` – Fuzzed binary input data  
- `gpt_output.txt` – Simulation output  
- `*_gpt.out` – Output log from simulator (e.g., Icarus Verilog)

Example:
```

alu/
├── alu.v
├── alu\_tb.v
├── alu\_gpt.py
├── inputs.txt
├── gpt\_output.txt
├── alu\_gpt.out

```

---

## 🔧 Tools Used

- Verilog HDL
- Icarus Verilog for simulation (`iverilog`, `vvp`)
- Python (for GPT-based input generation)
- Hugging Face Transformers (`GPT-2`)
- VS Code (as development environment)

---

## 🧠 Implemented RTL Modules

- ✅ ALU – Arithmetic Logic Unit
- ✅ MUX – 4-to-1 Multiplexer
- ✅ Counter – Up/Down counter with reset
- ✅ D Flip-Flop – With reset and enable
- ✅ FSM – Sequence detector (e.g., for 1011)
- ✅ Priority Encoder – 8-to-3 with valid output

---

## 🚀 How to Run (for any module)

1. Navigate into a module folder, e.g., `cd alu/`
2. Run GPT-based input generator:  
   `python3 alu_gpt.py`
3. Compile Verilog files:  
   `iverilog -o alu_gpt.out alu.v alu_tb.v`
4. Simulate the testbench:  
   `vvp alu_gpt.out`
5. View output in `gpt_output.txt`

---

## 📊 Goal

This project aims to:
- Improve RTL testbench coverage using ML-generated inputs
- Automate verification of digital designs
- Enable feedback-based enhancement for better simulation results

---

## 👤 Author

**Prince Solanki**  
Summer Research Intern – IIT Jodhpur  
SVNIT Surat – Department of ECE  
Email: u22ec139@eced.svnit.ac.in 


