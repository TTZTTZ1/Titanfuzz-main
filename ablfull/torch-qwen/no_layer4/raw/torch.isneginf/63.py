import torch

# Prepare valid input data
input_data = torch.tensor([-float('inf')], dtype=torch.float32)

# Call the API
result = torch.isneginf(input_data)
print(result)