import torch

# Prepare input data
input_tensor = torch.tensor([0, 0, 1, 0, 2])

# Call the API
result = input_tensor.nonzero(as_tuple=True)

print(result)