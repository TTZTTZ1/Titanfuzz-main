import torch

# Generate input data
tensor1 = torch.tensor([1.0, 2.0, 3.0])
tensor2 = torch.tensor([4.0, 5.0, 6.0])

# Call the API
result = tensor1.add_(tensor2)
print(result)