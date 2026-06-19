import torch

# Create a tensor and an index tensor
data = torch.tensor([[1, 2], [3, 4]])
index = torch.tensor([[0, 1], [1, 0]])

# Call torch.gather
result = torch.gather(data, 1, index)

print(result)