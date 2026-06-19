import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[-1+0j], [0+1j]])

# Task 3: Call the API
result = input_tensor.is_conj()

print(result)