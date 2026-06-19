import torch

# Prepare valid input data
input_tensor = torch.tensor([[0, 1], [2, 0]])

# Call the target API
result = input_tensor.nonzero(as_tuple=True)

print(result)