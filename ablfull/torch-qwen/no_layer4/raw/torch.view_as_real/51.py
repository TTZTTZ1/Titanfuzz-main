import torch

# Task 2: Generate input data
input_data = torch.tensor([1 + 1j, 2 + 2j], dtype=torch.complex64)

# Task 3: Call the API
result = torch.view_as_real(input_data)
print(result)