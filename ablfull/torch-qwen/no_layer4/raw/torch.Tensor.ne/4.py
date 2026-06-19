import torch

# Task 2: Generate input data
input_tensor = torch.tensor([1, 2, 3], dtype=torch.int)
other_value = 2

# Task 3: Call the API torch.Tensor.ne
result = input_tensor.ne(other_value)

print(result)