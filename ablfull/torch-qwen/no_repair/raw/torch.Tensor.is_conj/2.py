import torch

# Task 2: Generate input data
input_tensor = torch.tensor([1+1j, 2+2j])

# Task 3: Call the API
result = input_tensor.is_conj()

print(result)