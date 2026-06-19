import torch

# Generate valid input data
input_tensor = torch.randn(2, 3, 4)
new_order = (2, 0, 1)

# Call the API
result = input_tensor.permute(new_order)