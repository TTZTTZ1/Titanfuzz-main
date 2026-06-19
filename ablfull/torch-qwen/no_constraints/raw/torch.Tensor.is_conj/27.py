import torch

# Generate input data
input_data = torch.tensor([1+0j, 0+1j])

# Call the API
result = input_data.is_conj()

print(result)