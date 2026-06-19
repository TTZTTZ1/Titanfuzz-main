import torch

# Task 2: Generate input data
input_data = torch.randn(4, 5)

# Task 3: Call the API
result = torch.fft.fft(input_data)