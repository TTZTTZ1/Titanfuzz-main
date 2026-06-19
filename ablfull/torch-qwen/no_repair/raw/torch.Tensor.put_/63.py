import torch

index = torch.tensor([0, 1, 2])
source = torch.tensor([3, 4, 5])

# Ensure that the shapes of index and source match
assert index.shape == source.shape

# Prepare some tensor to be modified by put_()
data = torch.zeros(3)

# Call the API
data.put_(index, source)
print(data)