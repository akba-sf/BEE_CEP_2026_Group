# DC Circuit Solver Using Mesh Analysis
# BEE Course End Project - 2025-26
# Group Members:
#   Mohammed Akbar     - 25881A05Y4
#   Mohammed Rehan     - 25881A05AT
#   Shaik Shahrukh Ali - 25881A05BJ
# Course: A9205 - Basic Electrical Engineering Laboratory (VCE-R25)
# Language: Python

import numpy as np
import matplotlib.pyplot as plt

def get_resistance_matrix(n):
    print(f"\n--- Enter Resistance Matrix ({n}x{n}) ---")
    print("R[i][i] = sum of all resistors in mesh i")
    print("R[i][j] = negative of shared resistor between mesh i and mesh j")
    R = []
    for i in range(n):
        row = []
        for j in range(n):
            val = float(input(f"  Enter R[{i+1}][{j+1}] (Ohms): "))
            row.append(val)
        R.append(row)
    return np.array(R)

def get_voltage_vector(n):
    print(f"\n--- Enter Voltage Source Vector ({n} values) ---")
    print("V[i] = net voltage driving mesh i (positive if aiding, negative if opposing)")
    V = []
    for i in range(n):
        val = float(input(f"  Enter V[{i+1}] (Volts): "))
        V.append(val)
    return np.array(V)

def solve_mesh(R, V):
    det = np.linalg.det(R)
    if abs(det) < 1e-10:
        print("\nError: Resistance matrix is singular. Please check your circuit values.")
        return None
    I = np.linalg.solve(R, V)
    return I

def display_results(I, R, V, n):
    print("\n" + "="*50)
    print("              RESULTS")
    print("="*50)
    print("\n--- Mesh Currents ---")
    for i in range(n):
        direction = "clockwise" if I[i] >= 0 else "counter-clockwise"
        print(f"  I{i+1} = {I[i]:.4f} A  ({direction})")

    print("\n--- Voltage Drops Across Self-Resistances ---")
    for i in range(n):
        vdrop = R[i][i] * I[i]
        print(f"  Mesh {i+1}: V = R{i+1}{i+1} x I{i+1} = {R[i][i]} x {I[i]:.4f} = {vdrop:.4f} V")

    print("\n--- Power Consumed Per Mesh ---")
    for i in range(n):
        power = V[i] * I[i]
        print(f"  Mesh {i+1}: P = V{i+1} x I{i+1} = {V[i]} x {I[i]:.4f} = {power:.4f} W")

def plot_results(I, n):
    mesh_labels = [f"Mesh {i+1}\n(I{i+1})" for i in range(n)]
    colors = plt.cm.Set2(np.linspace(0, 1, n))

    plt.figure(figsize=(8, 5))
    bars = plt.bar(mesh_labels, I, color=colors, edgecolor='black', width=0.4)

    plt.title("DC Circuit Solver - Mesh Currents (Mesh Analysis)", fontsize=13, fontweight='bold')
    plt.xlabel("Mesh Number", fontsize=11)
    plt.ylabel("Current (Amperes)", fontsize=11)
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    for bar, val in zip(bars, I):
        ypos = bar.get_height() + 0.02 if val >= 0 else bar.get_height() - 0.08
        plt.text(bar.get_x() + bar.get_width()/2,
                 ypos,
                 f"{val:.4f} A",
                 ha='center', va='bottom', fontsize=10, fontweight='bold')

    plt.tight_layout()
    plt.savefig("screenshots/mesh_currents.png", dpi=150)
    plt.show()
    print("\nGraph saved as 'screenshots/mesh_currents.png'")

def main():
    print("="*50)
    print("   DC CIRCUIT SOLVER USING MESH ANALYSIS")
    print("   BEE Course End Project - 2025-26")
    print("   Group: Mohammed Akbar | Mohammed Rehan | Shaik Shahrukh Ali")
    print("="*50)

    while True:
        try:
            n = int(input("\nEnter number of independent meshes (2 to 5): "))
            if 2 <= n <= 5:
                break
            else:
                print("  Please enter a value between 2 and 5.")
        except ValueError:
            print("  Invalid input. Please enter a whole number.")

    R = get_resistance_matrix(n)
    V = get_voltage_vector(n)

    print("\n--- Input Summary ---")
    print("Resistance Matrix [R] (Ohms):")
    print(R)
    print("\nVoltage Vector [V] (Volts):")
    print(V)

    I = solve_mesh(R, V)

    if I is not None:
        display_results(I, R, V, n)
        plot_results(I, n)

    print("\n" + "="*50)
    print("         PROGRAM COMPLETED SUCCESSFULLY")
    print("="*50)

if __name__ == "__main__":
    main()
