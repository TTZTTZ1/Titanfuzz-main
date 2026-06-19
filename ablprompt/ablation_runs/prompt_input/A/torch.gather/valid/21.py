import torch

# Create some example tensors
indices = torch.tensor([[0, 2], [1, 0]])
values = torch.tensor([[3, 4, 5], [6, 7, 8]])

# Call torch.gather
result = torch.gather(values, 1, indices)

print(result)