import torch

# Task 2: Generate input data
input_tensor = torch.tensor([1, 2, 3])
other_value = torch.tensor([1, 0, 3])

# Task 3: Call the API torch.Tensor.ne
result = input_tensor.ne(other_value)
print(result)