import torch

# Prepare valid input data
data = [100] * 5  # Example sequence of integers

# Call the API
result = torch.QUInt8Storage(data)

print(result)