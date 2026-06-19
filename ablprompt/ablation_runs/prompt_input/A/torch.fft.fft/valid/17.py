import torch

# Create a sample tensor
x = torch.tensor([0.0, 1.0, 2.0, 3.0])

# Call the fft function from torch.fft
result = torch.fft.fft(x)

print(result)