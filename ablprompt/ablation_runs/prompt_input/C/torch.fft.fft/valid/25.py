import torch

# Create a random complex tensor
input_tensor = torch.randn(8)

# Compute the 1D FFT of the input tensor
fft_result = torch.fft.fft(input_tensor, n=16, dim=0, norm='ortho')

print("Input Tensor:", input_tensor)
print("FFT Result:", fft_result)