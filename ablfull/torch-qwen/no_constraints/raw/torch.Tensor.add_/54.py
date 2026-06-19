import torch

# Task 2: Generate input data
tensor_a = torch.tensor([1.0, 2.0, 3.0])
tensor_b = torch.tensor([4.0, 5.0, 6.0])

# Task 3: Call the API
result = tensor_a.add_(tensor_b)
print(result)