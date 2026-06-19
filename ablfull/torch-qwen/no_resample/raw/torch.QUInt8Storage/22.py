import torch

# Prepare valid input data
data = [10, 20, 30]  # Example sequence of integers within the range for QUInt8Storage

# Call the API
storage = torch.QUInt8Storage(data=data)

print(storage)