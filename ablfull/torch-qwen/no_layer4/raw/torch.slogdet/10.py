import torch

# Generate a valid input tensor
input_tensor = torch.randn(4, 4)

# Call the API
result = torch.slogdet(input_tensor)
print(result)