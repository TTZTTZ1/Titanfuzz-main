import torch

# Create a random tensor
x = torch.randn(4, 4, 4)

# Call fftn on the tensor
X = torch.fft.fftn(x)

print(X)