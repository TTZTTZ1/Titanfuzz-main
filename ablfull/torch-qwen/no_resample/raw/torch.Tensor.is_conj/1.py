import torch

# Task 2: Generate input data
input_data = torch.tensor([1+1j, 2+2j])

# Task 3: Call the API
result = input_data.is_conj()

print(result)