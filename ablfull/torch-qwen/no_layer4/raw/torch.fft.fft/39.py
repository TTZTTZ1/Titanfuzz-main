import torch

# Prepare valid input data
x = torch.tensor([1, 2, 3], dtype=torch.float32)

# Call the API
result = torch.fft.fft(x, dim=0)