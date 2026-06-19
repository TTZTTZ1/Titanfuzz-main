import torch

# Create a random complex tensor
input_tensor = torch.randn(8, 4) + 1j * torch.randn(8, 4)

# Compute the FFT
result = torch.fft.fft(input_tensor, n=16, dim=0, norm='ortho')

print(result)