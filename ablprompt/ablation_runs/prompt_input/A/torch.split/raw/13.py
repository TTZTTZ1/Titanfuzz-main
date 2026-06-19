import torch

# Create a tensor to split
tensor = torch.tensor([1, 2, 3, 4, 5, 6])

# Split the tensor into chunks of size 2
split_tensors = torch.split(tensor, 2)

# Print each split tensor
for i, split_tensor in enumerate(split_tensors):
    print(f"Split {i+1}: {split_tensor}")