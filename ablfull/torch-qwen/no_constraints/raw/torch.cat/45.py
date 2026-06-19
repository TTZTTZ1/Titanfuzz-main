import torch

# Task 2: Generate input data
tensor1 = torch.tensor([1.0, 2.0, 3.0])
tensor2 = torch.tensor([4.0, 5.0, 6.0])

# Task 3: Call the API torch.cat
result = torch.cat((tensor1, tensor2))

print(result)