import torch

# Generate input data
input_tensor = torch.tensor([[0, 2, 0], [3, 0, 4]])

# Call the API
result = input_tensor.nonzero(as_tuple=True)

print(result)