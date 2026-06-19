import torch

# Create a tensor and an index tensor
data = torch.tensor([[1, 2], [3, 4]])
indices = torch.tensor([[0, 1], [1, 0]])

# Call torch.gather
result = torch.gather(data, 1, indices)

print(result)