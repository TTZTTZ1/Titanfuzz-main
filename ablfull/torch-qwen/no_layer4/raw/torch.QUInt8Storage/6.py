import torch

# Prepare valid input data
data = [10, 20, 30, 40]  # Example sequence of integers

# Call the API
storage = torch.QUInt8Storage(data)