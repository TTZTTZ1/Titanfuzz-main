import torch

# Create a complex input tensor
input_tensor = torch.tensor([1 + 2j, 3 + 4j, 5 + 6j], dtype=torch.complex64)

# Compute the 1D discrete Fourier transform
fft_result = torch.fft.fft(input_tensor, n=8, dim=0, norm="ortho")

print(fft_result)