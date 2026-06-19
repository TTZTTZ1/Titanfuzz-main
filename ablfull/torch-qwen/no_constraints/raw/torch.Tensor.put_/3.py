import torch

# Prepare valid input data
tensor = torch.tensor([0., 1., 2., 3.])
indices = torch.tensor([0, 2])
values = torch.tensor([99., 88.])

# Call the API
tensor.put_(indices, values)

print(tensor)