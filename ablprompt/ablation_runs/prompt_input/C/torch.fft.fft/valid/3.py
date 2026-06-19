import torch

# Create a random complex tensor
input_tensor = torch.randn(8, 4, dtype=torch.complex64)

# Compute the 1D FFT along dimension 1
fft_result = torch.fft.fft(input_tensor, dim=1, norm="ortho")

print("Input Tensor:", input_tensor)
print("FFT Result:", fft_result)