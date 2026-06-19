import torch

# Prepare valid input data
data = [100] * 5  # Example sequence of integers

# Call the API
storage = torch.QUInt8Storage(data)