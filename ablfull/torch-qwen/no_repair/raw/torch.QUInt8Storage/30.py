import torch

# Prepare valid input data
data = [0, 1, 2, 3, 4]  # Example sequence of integers within the QUInt8 range (0-255)

# Call the API
storage = torch.QUInt8Storage(data)