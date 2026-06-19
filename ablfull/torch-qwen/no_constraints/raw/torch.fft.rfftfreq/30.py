import torch

# Task 2: Generate input data
n = 512  # Number of samples
d = 0.1  # Sample spacing

# Task 3: Call the API torch.fft.rfftfreq
result = torch.fft.rfftfreq(n, d)