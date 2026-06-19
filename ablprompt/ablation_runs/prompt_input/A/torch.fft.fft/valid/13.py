import torch

# Create a tensor
x = torch.tensor([1.0, 2.0, 3.0, 4.0])

# Call the torch.fft.fft function
fft_result = torch.fft.fft(x)

print("Input Tensor:", x)
print("FFT Result:", fft_result)