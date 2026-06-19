import torch

# Create a random complex tensor
input_tensor = torch.randn(8, 8, dtype=torch.complex64)

# Compute the 2D FFT of the input tensor
result = torch.fft.fft(input_tensor, n=8, dim=-1, norm="ortho")

print(result)