import torch

# Prepare valid input data
index = torch.tensor([0, 1, 2], dtype=torch.int)
source = torch.tensor([10, 20, 30], dtype=torch.int)

# Call the API
result_tensor = torch.zeros(5, dtype=torch.int)
result_tensor.put_(index, source)

print(result_tensor)