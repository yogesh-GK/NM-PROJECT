import torch
import time
import psutil
import os

# Create a simple model
model = torch.nn.Sequential(
    torch.nn.Linear(10, 5),
    torch.nn.ReLU(),
    torch.nn.Linear(5, 2)
)
model.eval()

# Create sample input
input_data = torch.randn(1, 10)

# Track process for CPU and memory
process = psutil.Process(os.getpid())

# Record CPU and memory before
cpu_before = process.cpu_percent(interval=None)
mem_before = process.memory_info().rss / (1024 ** 2)  # in MB

# Time the inference
start = time.time()
with torch.no_grad():
    output = model(input_data)
end = time.time()

# Record CPU and memory after
cpu_after = process.cpu_percent(interval=None)
mem_after = process.memory_info().rss / (1024 ** 2)

# Print performance metrics
print("=== Simple Performance Metrics ===")
print(f"Inference Time: {(end - start) * 1000:.2f} ms")
print(f"CPU Usage Change: {cpu_after - cpu_before:.2f} %")
print(f"Memory Usage Change: {mem_after - mem_before:.2f} MB")
