import torch

# Create some sample tensors
indices = torch.tensor([[0, 2], [1, 0]])
source_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Call torch.gather
result = torch.gather(source_tensor, 1, indices)

print(result)