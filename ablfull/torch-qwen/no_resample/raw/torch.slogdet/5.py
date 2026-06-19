import torch

# Generate a random square matrix of size 5x5 with float64 dtype
input_tensor = torch.randn(5, 5, dtype=torch.float64)

# Call torch.slogdet
result = torch.slogdet(input_tensor)
print(result)