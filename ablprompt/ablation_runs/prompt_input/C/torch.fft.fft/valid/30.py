import torch

# Create a random complex tensor
input_tensor = torch.randn(8, 4)

# Compute the 1D FFT along the first dimension
output_tensor = torch.fft.fft(input_tensor, dim=0, norm='ortho')

print(output_tensor)