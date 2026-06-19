import torch

# Create a tensor
tensor = torch.tensor([1, 2, 3, 4, 5, 6])

# Split the tensor into chunks of size 2
split_tensors = torch.split(tensor, 2)

# Print the split tensors
for i, t in enumerate(split_tensors):
    print(f"Chunk {i+1}: {t}")