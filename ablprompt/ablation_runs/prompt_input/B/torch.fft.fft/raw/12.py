import torch

# Create a random complex tensor
input_tensor = torch.randn(8, 8) + 1j * torch.randn(8, 8)

# Compute the 2D FFT
output_tensor = torch.fft.fft(input_tensor, dim=(0, 1), norm='ortho')

print(output_tensor)