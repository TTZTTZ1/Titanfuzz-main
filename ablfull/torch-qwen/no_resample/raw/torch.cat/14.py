import torch

# Task 2: Generate input data
tensor1 = torch.tensor([])
tensor2 = torch.tensor([1, 2, 3])
tensors = [tensor1, tensor2]

# Task 3: Call the API torch.cat
result = torch.cat(tensors, dim=0)
print(result)