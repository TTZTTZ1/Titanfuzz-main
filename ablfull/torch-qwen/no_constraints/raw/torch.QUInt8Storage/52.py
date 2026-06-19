import torch

# Prepare valid input data
data = [0, 127, 254]

# Call the API
storage = torch.QUInt8Storage(data)