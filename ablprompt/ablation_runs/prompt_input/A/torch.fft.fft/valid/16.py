import torch

# Create a tensor with complex numbers
x = torch.tensor([1 + 2j, 3 - 4j, 5 + 6j])

# Compute the FFT of the tensor
fft_result = torch.fft.fft(x)

print("Input tensor:", x)
print("FFT result:", fft_result)