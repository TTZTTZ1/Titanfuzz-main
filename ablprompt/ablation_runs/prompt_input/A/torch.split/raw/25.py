import torch

# Create a tensor to split
tensor = torch.tensor([1, 2, 3, 4, 5])

# Split the tensor into chunks of size 2
split_tensors = torch.split(tensor, 2)

# Print the result
print(split_tensors)