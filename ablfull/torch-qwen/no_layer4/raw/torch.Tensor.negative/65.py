import torch

# Prepare input data: create a tensor of floats
input_tensor = torch.tensor([1.0, -2.0, 3.0])

# Call the API
result = input_tensor.negative()

print(result)