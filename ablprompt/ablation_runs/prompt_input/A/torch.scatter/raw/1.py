import torch

# Create some example tensors
indices = torch.tensor([[0, 1], [2, 3]])
updates = torch.tensor([[99, -99], [-999, 999]])
input_tensor = torch.zeros((4, 4))

# Call torch.scatter
result = input_tensor.scatter(1, indices, updates)

print(result)