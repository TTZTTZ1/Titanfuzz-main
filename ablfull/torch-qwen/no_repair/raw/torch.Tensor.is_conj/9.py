import torch

# Generate input data
input_tensor = torch.tensor([1+0j, 2+0j, 3+0j])

# Call the API
result = input_tensor.is_conj()

print(result)