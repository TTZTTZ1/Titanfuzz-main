import torch

# Task 2: Generate input data
tensor1 = torch.tensor([1.0, 2.0])
tensor2 = torch.tensor([3.0, 4.0])

# Task 3: Call the API torch.add
result = torch.add(tensor1, tensor2)
print(result)