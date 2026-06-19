import torch

# Prepare input data
param_tensor = torch.tensor([0.1, -0.2, 0.3], requires_grad=True)
optimizer = torch.optim.SGD([param_tensor], lr=0.01, momentum=0.9)

# Call the API
optimizer.step()