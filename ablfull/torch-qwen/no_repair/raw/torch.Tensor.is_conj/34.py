import torch

# Generate input data
tensor = torch.tensor([[1+0j, 2+0j], [3+0j, 4+0j]])

# Call the API
result = tensor.is_conj()

print(result)