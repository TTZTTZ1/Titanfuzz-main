import torch

# Generate input data
input_data = torch.tensor([1+2j, 3+4j])

# Call the API
result = input_data.is_conj()

print(result)