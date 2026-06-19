import torch

# Generate a 2x2 tensor of random floats between -1 and 1
input_tensor = torch.randn(2, 2)

# Ensure the tensor is not singular by checking its determinant
while torch.det(input_tensor).item() == 0:
    input_tensor = torch.randn(2, 2)

# Call torch.slogdet
result = torch.slogdet(input_tensor)
print(result)