import torch

# Task 2: Generate input data
index = torch.tensor([0, 1, 2])
source = torch.tensor([10, 20, 30])

# Task 3: Call the API
result_tensor = torch.zeros(5)
result_tensor.put_(index, source)

print(result_tensor)