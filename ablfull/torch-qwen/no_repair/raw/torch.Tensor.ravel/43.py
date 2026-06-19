import torch

# Prepare valid input data
data = torch.tensor([[1, 2], [3, 4]])

# Call the target API
raveled_data = data.ravel()