import torch

# Create a random complex tensor
input_tensor = torch.randn(8, 4) + 1j * torch.randn(8, 4)

# Compute the FFT along dimension 0
fft_result = torch.fft.fft(input_tensor, dim=0, norm='ortho')

print(fft_result)