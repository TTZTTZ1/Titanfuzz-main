import torch

# Generate input data
input_tensor = torch.tensor([[0, 2, 0], [3, 0, 5]])

# Call the API
result = input_tensor.nonzero()

print(result)