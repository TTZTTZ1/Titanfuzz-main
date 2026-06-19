import torch

# Create a sample tensor
x = torch.tensor([0.0, 1.0, 2.0, 3.0], dtype=torch.float32)

# Compute the FFT of the tensor
fft_result = torch.fft.fft(x)

print("Input Tensor:", x)
print("FFT Result:", fft_result)