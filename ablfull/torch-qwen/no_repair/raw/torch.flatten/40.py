import torch

# Prepare valid input data
input_tensor = torch.tensor([[1, 2], [3, 4]])
start_dim = 0
end_dim = -1

# Call the API
result = torch.flatten(input_tensor, start_dim, end_dim)

print(result)