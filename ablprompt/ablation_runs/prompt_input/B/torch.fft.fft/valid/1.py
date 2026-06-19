import torch

# Create a random complex tensor
input_tensor = torch.randn(8, dtype=torch.complex64)

# Compute the 1D FFT
output_fft = torch.fft.fft(input_tensor, n=16, dim=0, norm='ortho')

print(output_fft)