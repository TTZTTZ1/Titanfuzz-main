import torch

# Generate a 3x3 tensor of random floats between -1 and 1
input_tensor = torch.randn(3, 3)

# Ensure the tensor is of type float (default)
input_tensor = input_tensor.float()

# Call torch.slogdet
result = torch.slogdet(input_tensor)

print(result)