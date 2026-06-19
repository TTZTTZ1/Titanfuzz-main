import torch

# Prepare valid input data
data = [1, 2, 3]

# Call the API
result = torch.QUInt8Storage(data)

print(result)