import torch

# Generate input data
data = torch.tensor([[1, 2], [3, 4]])

# Call the API
raveled_data = data.ravel()

print(raveled_data)