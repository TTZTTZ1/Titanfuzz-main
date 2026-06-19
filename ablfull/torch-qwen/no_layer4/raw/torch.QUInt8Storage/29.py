import torch

# Prepare valid input data
data = [100] * 5  # Example sequence of integers within the UINT8 range

# Call the API
storage = torch.QUInt8Storage(data)