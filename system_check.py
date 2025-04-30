import sys
import platform
import time

print(f"Python version: {sys.version}")
print(f"Platform: {platform.platform()}")
print(f"Python executable: {sys.executable}")

start_time = time.perf_counter()  # Using perf_counter for higher precision timing
print("Hello, World!")
end_time = time.perf_counter()    # Using perf_counter for higher precision timing
print(f"Execution time: {(end_time - start_time)*1000:.4f} ms")  # Increased decimal precision


start_time = time.perf_counter()  # Using perf_counter for higher precision timing
from openai import OpenAI
end_time = time.perf_counter()    # Using perf_counter for higher precision timing
print(f"Execution time: {(end_time - start_time)*1000:.4f} ms")  # Increased decimal precision
