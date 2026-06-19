import torch

# Prepare input data
input_data = torch.tensor([-1.5, -0.4, 0.4, 1.5])

# Call the API
result = torch.special.round(input_data)

print(result)