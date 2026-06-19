import torch

# Generate input data
input_tensor = torch.tensor([1, -2, 3])

# Call the API
result = input_tensor.negative()

print(result)