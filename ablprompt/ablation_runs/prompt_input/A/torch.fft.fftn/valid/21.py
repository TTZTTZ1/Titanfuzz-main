import torch

# Create a random tensor
input_tensor = torch.randn(4, 4, 4)

# Call the fftn function from torch.fft module
fft_result = torch.fft.fftn(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("FFT Result:")
print(fft_result)