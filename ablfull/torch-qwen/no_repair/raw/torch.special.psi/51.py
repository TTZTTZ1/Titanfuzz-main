import torch

# Generate a random tensor as input
input_tensor = torch.randn(5)

# Call torch.special.psi with the generated input
result = torch.special.psi(input_tensor)
print(result)