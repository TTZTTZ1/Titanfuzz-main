import torch

# Generate input data
input_tensor = torch.tensor([[0, 0], [0, 1]])

# Call the API
result = input_tensor.nonzero()

print(result)