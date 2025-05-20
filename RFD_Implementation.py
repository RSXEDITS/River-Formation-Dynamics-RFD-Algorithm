import numpy as np
import random

# Step 1: Define the cost function (what we want to minimize)
def cost_function(position):
    # Rastrigin function: used to test optimization algorithms
    return 10 * len(position) + sum([(x**2 - 10 * np.cos(2 * np.pi * x)) for x in position])

# Step 2: Initialize water drops (solutions)
def initialize_drops(num_drops, dimensions, bounds):
    drops = []
    for _ in range(num_drops):
        position = np.array([random.uniform(bounds[0], bounds[1]) for _ in range(dimensions)])
        drops.append(position)
    return drops

# Step 3: Simulate drop movement (toward best drop with erosion)
def move_drop(current_drop, best_drop, erosion_rate=0.2):
    direction = best_drop - current_drop
    step = erosion_rate * direction + np.random.normal(0, 0.01, size=len(current_drop))
    new_position = current_drop + step
    return new_position

# Step 4: River Formation Dynamics main function
def river_formation_dynamics(num_drops=5, dimensions=2, bounds=(-5.12, 5.12), max_iterations=30):
    drops = initialize_drops(num_drops, dimensions, bounds)
    best_drop = min(drops, key=cost_function)

    print("Initial Drop Positions and Costs:")
    for i, drop in enumerate(drops):
        print(f"Drop {i+1}: {drop} -> Cost: {cost_function(drop):.4f}")
    print("\nStarting RFD optimization...\n")

    for iteration in range(max_iterations):
        print(f"Iteration {iteration + 1}")
        for i in range(num_drops):
            new_position = move_drop(drops[i], best_drop)
            # Ensure the drop stays within bounds
            new_position = np.clip(new_position, bounds[0], bounds[1])

            if cost_function(new_position) < cost_function(drops[i]):
                print(f"  Drop {i+1} moved from {drops[i]} to {new_position}")
                drops[i] = new_position

        # Update best drop
        new_best = min(drops, key=cost_function)
        if cost_function(new_best) < cost_function(best_drop):
            print(f"  New best found: {new_best} with cost {cost_function(new_best):.4f}")
            best_drop = new_best
        print()

    print("Final Best Solution:")
    print(f"Position: {best_drop}")
    print(f"Cost: {cost_function(best_drop):.4f}")

# Step 5: Run the algorithm
river_formation_dynamics()
