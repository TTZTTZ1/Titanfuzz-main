import torch

# Task 2: Generate input data
tensor1 = torch.randn(3)
tensor2 = torch.randn(3)

# Task 3: Call the API torch.cat
result = torch.cat((tensor1, tensor2))