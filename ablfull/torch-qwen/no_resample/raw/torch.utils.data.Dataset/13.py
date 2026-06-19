import torch

# Generate input data (empty dictionary as Dataset does not require parameters)
input_data = {}

# Call the API
dataset = torch.utils.data.Dataset(**input_data)