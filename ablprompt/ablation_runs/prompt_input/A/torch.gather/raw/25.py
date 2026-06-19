import torch

# Create a tensor
tensor = torch.tensor([[1, 2], [3, 4]])

# Define indices to gather from the tensor
indices = torch.tensor([[0, 1], [1, 0]])

# Call torch.gather
result = torch.gather(tensor, 1, indices)

print(result)