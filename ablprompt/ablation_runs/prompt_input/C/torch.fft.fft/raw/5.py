import torch

# Create a complex input tensor
input_tensor = torch.tensor([1 + 2j, 3 + 4j, 5 + 6j, 7 + 8j])

# Compute the 1D FFT
fft_result = torch.fft.fft(input_tensor)

print("Input Tensor:", input_tensor)
print("FFT Result:", fft_result)