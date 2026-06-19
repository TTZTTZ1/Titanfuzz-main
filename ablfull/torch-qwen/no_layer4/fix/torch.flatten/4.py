import torch
input_tensor = torch.randn(2, 3, 4)
start_dim = 1
end_dim = 2
flattened_tensor = torch.flatten(input_tensor, start_dim=start_dim, end_dim=end_dim)
print(flattened_tensor)