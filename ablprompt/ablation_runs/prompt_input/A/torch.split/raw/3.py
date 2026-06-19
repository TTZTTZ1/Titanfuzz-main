import torch

# Create a tensor
tensor = torch.randn(10)

# Split the tensor into 2 parts
split_tensors = torch.split(tensor, 5)

print(split_tensors)