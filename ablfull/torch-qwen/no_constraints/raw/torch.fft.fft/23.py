import torch

# Generate input data
input_data = torch.tensor([0, 1, 2, 3], dtype=torch.float32)

# Call the API
result = torch.fft.fft(input_data)