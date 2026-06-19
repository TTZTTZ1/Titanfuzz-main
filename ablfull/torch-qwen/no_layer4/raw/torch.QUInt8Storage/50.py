import torch

# Generate input data
data = [0, 1, 2, 3, 4, 5]

# Call the API
result = torch.QUInt8Storage(data)

print(result)