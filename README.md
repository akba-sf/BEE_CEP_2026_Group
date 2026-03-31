# DC Circuit Solver Using Mesh Analysis
**Course:** A9205 - Basic Electrical Engineering Lab (VCE-R25)
**Academic Year:** 2025-26 | I B.Tech. II Sem | CSE-F

## Group Members
| Name | Roll No |
|------|---------|
| Member 1 | XXXXXXXX |
| Member 2 | XXXXXXXX |

## Problem Description
Solves DC circuits with multiple independent mesh loops using KVL-based Mesh Analysis.

## Mathematical Formulation
[R] × [I] = [V]  →  [I] = [R]⁻¹[V]

## How to Run
```bash
pip install numpy matplotlib
python src/dc_mesh_solver.py
```

## Sample Output
Mesh 1 Current: 2.3750 A (clockwise)
Mesh 2 Current: 1.6250 A (clockwise)

Submission Deadline
📅 01-05-2026
Would you like me to help you with any specific part — the report (PDF), the flowchart, the README, or extending the code to handle more complex circuits?i have created repoistry10:21 AMGreat work! 🎉 Your GitHub repository BEE_CEP_2026_Group is created and live. Now let's set it up properly.
Here's exactly what you need to do next:

✅ Step-by-Step: Set Up Your Repository
Step 1 — Update README.md
Click the pencil (edit) icon on the README, delete everything, and paste this:
markdown# DC Circuit Solver Using Mesh Analysis

**Course:** A9205 - Basic Electrical Engineering Laboratory (VCE-R25)  
**Academic Year:** 2025-26 | I B.Tech. II Semester | CSE-F  
**Project Type:** Programming-Based Analytical Model  

---

## 👥 Group Members

|  Name             |  Roll No    |
|---------------------------------|
| Mohammed Akbar    | 25881A05Y4  |
| Mohammed Rehan    | 25881A05AT  |
| Shaik Shahrukh Ali| 25881A05BJ  |

---

## 📌 Problem Description

This project solves DC circuits with multiple independent mesh loops using  
**Mesh Analysis (KVL-based)**. The program accepts resistor values and voltage  
sources, builds the resistance matrix, and computes mesh currents using matrix inversion.

---

## 📐 Mathematical Formulation

Mesh Analysis applies KVL to each loop:

**[R] × [I] = [V]**

- [R] = Resistance matrix (n × n)
- [I] = Unknown mesh current vector
- [V] = Voltage source vector

**Solution:** [I] = [R]⁻¹ × [V]

---

## 📁 Repository Structure
```
BEE_CEP_2026_Group/
├── src/
│   └── dc_mesh_solver.py
├── report/
│   └── BEE_CEP_Report.pdf
├── screenshots/
│   └── mesh_currents.png
├── README.md
└── requirements.txt
```

---

## ▶️ How to Run
```bash
pip install numpy matplotlib
python src/dc_mesh_solver.py
```

---

## 📊 Sample Output
```
Mesh 1 Current (I1) = 2.3750 A  (clockwise)
Mesh 2 Current (I2) = 1.6250 A  (clockwise)
```

---

## 📚 References

- Basic Electrical Engineering - D.C. Kulshreshtha, TMH
- Engineering Circuit Analysis - Hayt & Kemmerly
