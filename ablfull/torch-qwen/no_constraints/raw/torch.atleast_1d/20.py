import torch

# Generate input data
input_data = [5, 6]

# Call the API
result = torch.atleast_1d(*input_data)

print(result)