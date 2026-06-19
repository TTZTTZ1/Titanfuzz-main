import torch

# Create a sample tensor
x = torch.tensor([0, 1, 2, 3])

# Call the FFT function
fft_result = torch.fft.fft(x)

print("Input Tensor:", x)
print("FFT Result:", fft_result)