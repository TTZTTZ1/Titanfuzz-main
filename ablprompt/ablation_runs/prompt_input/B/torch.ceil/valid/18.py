import torch

# Create a tensor with both integer and float values
input_tensor = torch.tensor([-1.2, 3.5, 4.0])

# Apply torch.ceil to the tensor
result_tensor = torch.ceil(input_tensor)

print(result_tensor)