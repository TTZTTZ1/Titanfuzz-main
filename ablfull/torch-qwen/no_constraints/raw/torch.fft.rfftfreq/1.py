import torch

# Task 2: Generate input data
n = 50  # Number of samples

# Task 3: Call the API
result = torch.fft.rfftfreq(n)
print(result)