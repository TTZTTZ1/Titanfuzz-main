import torch

# Create a random tensor
input_tensor = torch.randn(10)

# Call the fft function from torch.fft module
fft_result = torch.fft.fft(input_tensor)

print("Input Tensor:", input_tensor)
print("FFT Result:", fft_result)