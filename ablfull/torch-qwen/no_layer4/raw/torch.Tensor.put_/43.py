import torch

# Prepare valid input data
index = torch.tensor([0, 1, 2])
source = torch.tensor([10, 20, 30])

# Call the API
result = torch.Tensor(5).put_(index, source)
print(result)