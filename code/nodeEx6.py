import numpy as np

# Define the resistances (in ohms)
R1 = 12  # Resistance of R1
R2 = 6   # Resistance of R2
R3 = 5   # Resistance of R3
R4 = 3   # Resistance of R4
R5 = 4   # Resistance of R5

# Define the current sources (in amperes)
IS1 = 1  # Current source entering Node 1
IS2 = 4  # Current source leaving Node 2

# Calculate the conductances (G = 1/R)
G1 = 1 / R1
G2 = 1 / R2
G3 = 1 / R3
G4 = 1 / R4
G5 = 1 / R5

# Define the G matrix
G = np.array([
    [G1 + G2 + G5, -G2,          -G5],
    [-G2,          G2 + G3,      -G3],
    [-G5,          -G3,          G3 + G4 + G5]
])

# Define the current vector (I)
I = np.array([
    IS1,
    -IS2,
    0
])

# Solve for the node voltages (V)
V = np.linalg.solve(G, I)

# Display the results
print("Node Voltages (V):")
print(V)