import torch

# Create a random tensor
tensor = torch.randn(4, 4, 4)

# Compute the N-dimensional FFT of the tensor
fft_result = torch.fft.fftn(tensor)

print(fft_result)