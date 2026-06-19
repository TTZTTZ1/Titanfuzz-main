import torch

# Generate a 2x2 tensor of random floats between -1 and 1
input_tensor = torch.randn(2, 2)

# Ensure the tensor is of type float
input_tensor = input_tensor.float()

# Call torch.slogdet
result = torch.slogdet(input_tensor)
print(result)