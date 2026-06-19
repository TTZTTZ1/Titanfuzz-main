import torch

# Task 2: Generate input data
input_data = torch.tensor([0.0, 1.0, 2.0, 3.0], dtype=torch.float32)

# Task 3: Call the API torch.fft.fft
result = torch.fft.fft(input_data)
print(result)