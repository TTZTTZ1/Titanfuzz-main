import torch

# Task 2: Generate input data
n = 512
d = 0.1

# Task 3: Call the API
result = torch.fft.rfftfreq(n, d)