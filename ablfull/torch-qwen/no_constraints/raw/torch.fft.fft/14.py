import torch

# Task 2: Generate input data
x = torch.tensor([0.5, -0.2, 0.8, -0.4])

# Task 3: Call the API torch.fft.fft
result = torch.fft.fft(x)