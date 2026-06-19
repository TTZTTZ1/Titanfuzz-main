import torch

# Task 2: Generate input data
input_data = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

# Task 3: Call the API torch.fft.fft
result = torch.fft.fft(input_data)

print(result)