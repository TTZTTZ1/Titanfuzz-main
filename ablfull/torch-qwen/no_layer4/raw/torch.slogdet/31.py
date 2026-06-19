import torch

# Generate a random square matrix of size 3x3 with double precision
input_data = torch.randn(3, 3, dtype=torch.double)

# Call torch.slogdet
result = torch.slogdet(input_data)
print(result)