import torch

# Create a random complex tensor
input_tensor = torch.randn(8, 4, 2)

# Compute the 1D FFT along dimension 1 with normalization 'ortho'
fft_result = torch.fft.fft(input_tensor, dim=1, norm='ortho')

print(fft_result)