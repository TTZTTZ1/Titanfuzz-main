import torch

# Prepare input data
index = torch.tensor([0, 1, 2])
source = torch.tensor([4, 5, 6], dtype=torch.float)
accumulate = False

# Call the API
result_tensor = torch.zeros(5)
result_tensor.put_(index, source, accumulate=accumulate)

print(result_tensor)