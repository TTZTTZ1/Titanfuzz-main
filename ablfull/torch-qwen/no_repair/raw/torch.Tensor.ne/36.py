import torch

# Task 2: Generate input data
input_tensor = torch.tensor([1, 2, 3], dtype=torch.float)
other_value = 2.0

# Task 3: Call the API
result = input_tensor.ne(other_value)

print(result)