import torch

# Prepare valid input data
data = torch.tensor([0, 127], dtype=torch.uint8)

# Call the API
storage = torch.QUInt8Storage(data=data)