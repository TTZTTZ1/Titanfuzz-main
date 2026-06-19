import torch

# Generate input data
input_data = torch.tensor([1+1j, 2+2j])

# Call the API
result = input_data.is_conj()

print(result)