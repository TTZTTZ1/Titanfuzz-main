import torch

# Task 2: Generate input data
a = torch.tensor([[4., 7.], [2., 6.]], dtype=torch.float32)

# Task 3: Call the API torch.linalg.inv_ex
result = torch.linalg.inv_ex(a)
print(result)