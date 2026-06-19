import torch

# Create a sample tensor
x = torch.tensor([0, 1, 2, 3], dtype=torch.complex64)

# Call torch.fft.fft
result = torch.fft.fft(x)

print(result)