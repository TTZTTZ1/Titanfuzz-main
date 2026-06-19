import torch

# Create a random complex tensor
input_tensor = torch.randn(8, 4, 2)

# Compute the 1D FFT along dimension 1 with normalization 'ortho'
output_tensor = torch.fft.fft(input_tensor, dim=1, norm='ortho')

print(output_tensor)