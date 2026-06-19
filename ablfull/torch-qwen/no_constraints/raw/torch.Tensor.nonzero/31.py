import torch

# Prepare valid input data
input_tensor = torch.tensor([[0, 1], [2, 0]])

# Call the API
result = input_tensor.nonzero()

print(result)