import torch

# Task 2: Generate valid input data
tensor1 = torch.tensor([1.0, 2.0, 3.0])
tensor2 = torch.tensor([4.0, 5.0, 6.0])

# Task 3: Call the API
result = torch.Tensor.cross(tensor1, tensor2)
print(result)