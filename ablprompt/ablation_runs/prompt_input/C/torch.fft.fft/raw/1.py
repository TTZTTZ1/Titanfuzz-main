import torch

# Create a random complex tensor
input_tensor = torch.randn(8, 4, dtype=torch.complex64)

# Compute the FFT along dimension 1
fft_result = torch.fft.fft(input_tensor, dim=1, norm='ortho')

print(fft_result)