import torch

# Create a tensor where we will scatter values
tensor = torch.zeros(5, 5)

# Define the indices and source tensors for scattering
indices = torch.tensor([[0, 2], [1, 3]])
source = torch.tensor([[1, 1], [2, 2]])

# Call torch.scatter to update the tensor
result = torch.scatter(tensor, 1, indices, source)

print(result)