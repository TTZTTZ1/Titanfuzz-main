import torch

# Task 2: Generate input data
input_data = torch.tensor([0., 1., 2., 3.])

# Task 3: Call the API torch.fft.fft
result = torch.fft.fft(input_data)

print(result)