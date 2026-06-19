import torch

# Prepare valid input data
data = [1, 2, 3, 4, 5]  # Example sequence of integers

# Call the API
storage = torch.QUInt8Storage(data)