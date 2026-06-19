import torch

# Task 2: Generate input data
n = 8  # Number of points in the array

# Task 3: Call the API
result = torch.fft.rfftfreq(n)
print(result)