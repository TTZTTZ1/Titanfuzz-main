import torch

# Prepare valid input data
input_tensor = torch.tensor([[0, 0], [1, 2]])

# Call the API with specified parameters
result = input_tensor.nonzero(as_tuple=True)

print(result)