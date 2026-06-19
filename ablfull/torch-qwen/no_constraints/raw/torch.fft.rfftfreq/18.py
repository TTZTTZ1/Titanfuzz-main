import torch

# Task 2: Generate input data
n = 8  # Number of points in the sample
d = 0.5  # Sample spacing

# Task 3: Call the API
result = torch.fft.rfftfreq(n, d)
print(result)