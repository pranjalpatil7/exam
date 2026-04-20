def mcp(x1, x2, w, theta):
    net = x1 * w[0] + x2 * w[1]
    return 1 if net >= theta else 0


def run_gate(name, weights, theta):
    print(f"\n{name} Gate")
    print("Inputs -> Output")

    for x1, x2 in [(0,0), (0,1), (1,0), (1,1)]:
        output = mcp(x1, x2, weights, theta)
        print(f"({x1},{x2}) -> {output}")


# Fixed weights (MCP does NOT learn, only threshold changes)
w = [1, 1]

# Different logic gates using thresholds
run_gate("AND", w, 2)
run_gate("OR", w, 1)
run_gate("NAND", w, 0)
run_gate("NOR", [-1, -1], 0)

#pip install numpy

# AND Gate
# Inputs -> Output
# (0,0) -> 0
# (0,1) -> 0
# (1,0) -> 0
# (1,1) -> 1

# OR Gate
# Inputs -> Output
# (0,0) -> 0
# (0,1) -> 1
# (1,0) -> 1
# (1,1) -> 1

# NAND Gate
# Inputs -> Output
# (0,0) -> 1
# (0,1) -> 1
# (1,0) -> 1
# (1,1) -> 1

# NOR Gate
# Inputs -> Output
# (0,0) -> 1
# (0,1) -> 0
# (1,0) -> 0