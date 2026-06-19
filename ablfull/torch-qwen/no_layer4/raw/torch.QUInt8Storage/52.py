import torch

# Prepare valid input data
data = [42, 0, 255]

# Call the API
storage = torch.QUInt8Storage(data)

print(storage)