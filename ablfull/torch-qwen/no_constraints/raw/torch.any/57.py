import torch

# Generate input data: a tensor with at least one element set to True
input_tensor = torch.tensor([False, False, True])

# Call the API
result = torch.any(input_tensor)

print(result)