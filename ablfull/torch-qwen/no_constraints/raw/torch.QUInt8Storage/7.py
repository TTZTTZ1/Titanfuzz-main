import torch

# Generate valid input data
data = [0, 1, 254, 255]

# Call the API
storage = torch.QUInt8Storage(data=data)