import torch

# Task 2: Generate input data
input_data = torch.tensor([[[[1+2j, 3+4j], [5+6j, 7+8j]]]], dtype=torch.complex64)

# Task 3: Call the API
result = input_data.is_conj()

print(result)