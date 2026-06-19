import torch

# Prepare input data
input_data = torch.tensor([-1.7, -0.5, 0.2, 1.8])

# Call the API
result = torch.ceil(input_data)

print(result)