import torch

# Task 2: Generate input data
n = 50  # Number of samples
d = 1   # Sample spacing

# Task 3: Call the API
result = torch.fft.rfftfreq(n, d)
print(result)