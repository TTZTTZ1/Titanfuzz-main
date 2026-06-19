import torch

# Create a tensor
tensor = torch.tensor([[10, 2], [3, 4]])

# Call torch.argmin to find the index of the minimum value in the tensor
min_index = torch.argmin(tensor)

print("Index of the minimum value:", min_index)