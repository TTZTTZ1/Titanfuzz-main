import torch

# Prepare input data
input_data = [0, 1, 2, 3]

# Call the API
result = torch.QUInt8Storage(input_data)

print(result)