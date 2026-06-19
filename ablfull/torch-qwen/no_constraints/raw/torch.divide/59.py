import torch

# Generate valid input data
tensor1 = torch.tensor([4.0, 3.0, 2.0])
tensor2 = torch.tensor([2.0, 1.0, 1.0])

# Call the API
result = torch.divide(tensor1, tensor2)

print(result)