import torch

# Create a complex tensor
x = torch.tensor([1 + 2j, 3 + 4j, 5 + 6j])

# Compute the FFT
result = torch.fft.fft(x)

print(result)