import sys
import os
import time
import tracemalloc
import matplotlib.pyplot as plt

def allocate_memory(n_steps=20, step_size_mb=1):
    """Simulate heap growth by allocating blocks of memory over time."""
    blocks = []
    memory_usage = []

    tracemalloc.start()
    for i in range(n_steps):
        # Allocate about step_size_mb megabytes each step
        blocks.append(bytearray(step_size_mb * 1024 * 1024))
        current, peak = tracemalloc.get_traced_memory()
        memory_usage.append(current / (1024**2))  # Convert to MB
        print(f"Step {i+1}: Current={current / 1024**2:.2f} MB, Peak={peak / 1024**2:.2f} MB")
        time.sleep(0.2)

    tracemalloc.stop()
    return memory_usage

def plot_heap_growth(memory_usage):
    """Plot memory usage over time."""
    plt.figure(figsize=(8, 4))
    plt.plot(memory_usage, marker='o', label="Heap usage (MB)")
    plt.title("Python Heap Growth Over Time")
    plt.xlabel("Allocation step")
    plt.ylabel("Memory usage (MB)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def system_info():
    print(f"\nProcess ID: {os.getpid()}")
    print("To inspect stack/heap mappings on macOS, run in Terminal:")
    print(f"    vmmap {os.getpid()}")
    print("This will show regions labeled 'STACK', 'HEAP', and 'MALLOC ZONE'.")

if __name__ == "__main__":
    print("=== HEAP GROWTH DEMO ===")
    system_info()
    usage = allocate_memory()
    plot_heap_growth(usage)
