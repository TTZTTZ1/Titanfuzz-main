import torch

# Prepare valid input data
tensor1 = torch.tensor([[1, 0, 0], [0, 1, 0]])
tensor2 = torch.tensor([[0, 0, 1], [1, 0, 0]])

# Call the API
result = tensor1.cross(tensor2)

print(result)