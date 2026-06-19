import torch

# Prepare valid input data
input_tensor = torch.tensor([-float('inf'), float('nan')])

# Call the target API
result = torch.isneginf(input_tensor)

print(result)