import torch

# Prepare valid input data
data = [100]  # Example sequence of integers within QUInt8 range (0-255)

# Call the API
result = torch.QUInt8Storage(data)
print(result)