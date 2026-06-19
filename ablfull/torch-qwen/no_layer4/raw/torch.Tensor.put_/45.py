import torch

# Generate input data
index = torch.tensor([0, 1, 2])
source = torch.tensor([4, 5, 6], dtype=torch.float)

# Call the API
result = torch.zeros(3)
result.put_(index, source)
print(result)