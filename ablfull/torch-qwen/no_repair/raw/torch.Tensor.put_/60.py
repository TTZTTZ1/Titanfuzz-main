import torch

# Generate input data
index = torch.tensor([0, 2, 4])
source = torch.tensor([7, 8, 9])

# Call the API
result = torch.zeros(5, dtype=torch.int)
result.put_(index, source)

print(result)