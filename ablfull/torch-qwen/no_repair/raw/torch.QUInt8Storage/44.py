import torch

# Prepare valid input data
args = [10]

# Call the API
result = torch.QUInt8Storage(*args)
print(result)