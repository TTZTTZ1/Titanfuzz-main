import torch

# Generate input data: create a tensor of random floats between -1 and 1
input_data = torch.rand(5) * 2 - 1

# Call the API
result = input_data.double()