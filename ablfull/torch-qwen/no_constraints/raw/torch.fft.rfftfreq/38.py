import torch

# Task 2: Generate input data
N = 64  # Number of points
dN = 0.5  # Sample spacing

# Task 3: Call the API
result = torch.fft.rfftfreq(N, d=dN)
print(result)