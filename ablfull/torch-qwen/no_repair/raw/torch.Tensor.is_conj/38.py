import torch

# Generate input data
input_tensor = torch.tensor([1+1j, 2+2j], dtype=torch.complex64)

# Call the API
result = input_tensor.is_conj()

print(result)