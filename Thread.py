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
thread3 = threading.Thread(target=worker, args=("C", 0.5))
thread4 = threading.Thread(target=worker, args=("D", 2))
thread5 = threading.Thread(target=worker, args=("E", 1.2))

# Start threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

# Wait for both threads to finish
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()

print("All threads have finished.")
