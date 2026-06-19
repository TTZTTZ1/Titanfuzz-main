import torch

# Create a random tensor
x = torch.randn(4, 4, 4)

# Call the fftn function
result = torch.fft.fftn(x)

print(result)