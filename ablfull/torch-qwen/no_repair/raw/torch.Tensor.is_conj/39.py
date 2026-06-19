import torch

# Task 2: Generate input data
tensor = torch.tensor([[1+0j, 2+0j], [3+0j, 4+0j]])

# Task 3: Call the API
result = tensor.is_conj()

print(result)