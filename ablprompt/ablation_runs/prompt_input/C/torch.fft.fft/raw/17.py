import torch

# Create a random complex tensor
input_tensor = torch.randn(8, 4) + 1j * torch.randn(8, 4)

# Compute the 1D FFT along the first dimension
fft_result = torch.fft.fft(input_tensor, dim=0, norm='ortho')

print("Input Tensor:", input_tensor)
print("FFT Result:", fft_result)