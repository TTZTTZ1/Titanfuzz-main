import torch

# Task 2: Generate input data
input_tensor = torch.tensor([1+2j, 3+4j], dtype=torch.complex64)

# Task 3: Call the API
result = input_tensor.is_conj()

print(result)