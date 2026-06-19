import torch

# Prepare input data
index = torch.tensor([0, 1, 2], dtype=torch.int)
source = torch.tensor([4, 5, 6], dtype=torch.float)

# Call the API
result_tensor = torch.zeros(3)
result_tensor.put_(index, source, accumulate=False)
print(result_tensor)