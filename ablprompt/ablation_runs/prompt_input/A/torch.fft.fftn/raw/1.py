import torch

# Create a random tensor
input_tensor = torch.randn(4, 5, 6)

# Call the fftn function from torch.fft
fft_result = torch.fft.fftn(input_tensor)

print("Input Tensor:", input_tensor)
print("FFT Result:", fft_result)