import sys
import os
import tracemalloc

# --- Stack-like behavior in Python ---
# Function calls create new frames (Python + C stack frames)
def stack_demo(n):
    if n == 0:
        print("Reached bottom of recursion.")
        return
    frame_info = sys._getframe()  # gets current call frame
    print(f"Recursion depth: {n}, Frame object id: {id(frame_info)}")
    stack_demo(n - 1)

# --- Heap allocations ---
# Python objects (lists, dicts, etc.) are allocated on the heap
def heap_demo():
    a = [i for i in range(10_000)]  # allocate a big list on the heap
    print(f"List 'a' address (id): {id(a)}")
    print(f"Approximate memory usage of list: {sys.getsizeof(a)} bytes")

# --- Memory tracking using tracemalloc ---
def memory_tracking_demo():
    tracemalloc.start()
    before = tracemalloc.take_snapshot()

    x = [bytearray(1024 * 1024) for _ in range(10)]  # allocate ~10 MB
    after = tracemalloc.take_snapshot()

    stats = after.compare_to(before, 'lineno')
    top = stats[0]
    print("\nTop memory allocation:")
    print(top)

    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 1024**2:.2f} MB; Peak: {peak / 1024**2:.2f} MB")
    tracemalloc.stop()

# --- System info (macOS) ---
def system_info():
    print(f"\nProcess ID: {os.getpid()}")
    print("You can inspect this process externally using:")
    print(f"    vmmap {os.getpid()}  # macOS command to view stack/heap mappings")

if __name__ == "__main__":
    print("=== STACK DEMO ===")
    stack_demo(3)

    print("\n=== HEAP DEMO ===")
    heap_demo()

    print("\n=== MEMORY TRACKING ===")
    memory_tracking_demo()

    print("\n=== SYSTEM INFO ===")
    system_info()
