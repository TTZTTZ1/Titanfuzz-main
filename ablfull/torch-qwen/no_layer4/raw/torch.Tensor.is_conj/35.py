import torch

# Task 2: Generate input data
input_data = torch.tensor([1+0j, 0+1j])

# Task 3: Call the API torch.Tensor.is_conj
result = input_data.is_conj()

print(result)