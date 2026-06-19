import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[-1+0j, 2+0j], [3+4j, -5+6j]])

# Task 3: Call the API
result = input_tensor.is_conj()

print(result)