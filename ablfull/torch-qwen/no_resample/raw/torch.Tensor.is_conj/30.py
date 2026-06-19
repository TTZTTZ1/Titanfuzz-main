import torch

# Generate input data
input_tensor = torch.tensor([1+2j, 3+4j])

# Call the API
result = input_tensor.is_conj()

print(result)