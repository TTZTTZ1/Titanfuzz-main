import torch

# Create some example tensors
indices = torch.tensor([[0, 2], [1, 3]])
source = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])

# Call torch.gather
result = torch.gather(source, 1, indices)

print(result)