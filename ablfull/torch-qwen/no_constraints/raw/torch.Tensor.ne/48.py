import torch

# Prepare valid input data
a = torch.tensor([1, 2, 3])
b = torch.tensor([1, 0, 3])

# Call the API
result = a.ne(b)
print(result)