import torch

# Prepare valid input data
tensor1 = torch.tensor([4.0])
tensor2 = torch.tensor([2.0])

# Call the API
result = torch.divide(tensor1, tensor2)
print(result)