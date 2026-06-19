import torch

# Task 2: Generate input data
input_tensor = torch.tensor([1, 2, 3], dtype=torch.int64)
other_value = 2

# Task 3: Call the API
result = input_tensor.ne(other_value)

print(result)