import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[1, 2], [3, 4]])
repeats_value = 2
dim_value = 0

# Task 3: Call the API
result = torch.repeat_interleave(input=input_tensor, repeats=repeats_value, dim=dim_value)
print(result)