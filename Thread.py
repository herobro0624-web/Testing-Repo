import threading
import time

def worker(name, delay):
    """A simple worker function"""
    for i in range(3):
        time.sleep(delay)
        print(f"Worker {name}: iteration {i+1}")

# Create threads
thread1 = threading.Thread(target=worker, args=("A", 1))
thread2 = threading.Thread(target=worker, args=("B", 1.5))

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("All threads have finished.")
