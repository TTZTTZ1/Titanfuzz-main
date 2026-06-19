import torch

# Generate input data (empty dictionary as Dataset does not require parameters)
data = {}

# Call the API
dataset = torch.utils.data.Dataset(**data)