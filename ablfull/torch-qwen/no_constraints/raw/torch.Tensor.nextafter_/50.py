import torch

# Prepare valid input data
x = torch.tensor([1.0])
y = torch.tensor([2.0])

# Call the target API
result = x.nextafter(y)

print(result)