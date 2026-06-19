import torch

# Generate input data
input_data = torch.tensor(5)

# Call the API
result = torch.atleast_1d(input_data)
print(result)