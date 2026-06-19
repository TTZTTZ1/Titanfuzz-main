import torch

# Prepare valid input data
data = [0, 127]  # A sequence of integers within the QUInt8 range

# Call the API
result = torch.QUInt8Storage(data)

print(result)