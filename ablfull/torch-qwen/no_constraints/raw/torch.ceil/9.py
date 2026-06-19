import torch

# Generate input data
input_data = torch.tensor([-1.5, 0.3, 2.7])

# Call the API
result = torch.ceil(input_data)

print(result)