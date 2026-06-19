import torch

# Task 2: Generate input data
n = 50
d = 1.0

# Task 3: Call the API
result = torch.fft.rfftfreq(n, d)
print(result)