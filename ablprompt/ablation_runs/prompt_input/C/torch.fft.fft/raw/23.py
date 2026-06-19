import torch

# Create a random complex tensor
input_tensor = torch.randn(8, 4, dtype=torch.complex64)

# Compute the 1D FFT along dimension 0 with normalization 'ortho'
fft_result = torch.fft.fft(input_tensor, dim=0, norm='ortho')

print(fft_result)