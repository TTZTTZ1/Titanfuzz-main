import torch

# Task 2: Generate input data
tensor1 = torch.tensor([])
tensor2 = torch.tensor([1, 2, 3])

# Task 3: Call the API torch.cat
result = torch.cat((tensor1, tensor2), dim=0)
print(result)