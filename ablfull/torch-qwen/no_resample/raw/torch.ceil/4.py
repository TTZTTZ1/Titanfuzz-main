import torch

# Prepare valid input data
input_data = torch.tensor([-1.5, 0.2, 3.7])

# Call the API
result = torch.ceil(input_data)

print(result)