import torch

# Create a tensor to scatter values into
tensor = torch.zeros(5, 5)

# Define the indices and source values for scattering
indices = torch.tensor([[0, 2], [1, 3]])
values = torch.tensor([[1, 2], [3, 4]])

# Call torch.scatter
result = torch.scatter(tensor, 1, indices, values)

print(result)