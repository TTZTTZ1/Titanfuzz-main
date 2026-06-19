import torch

# Prepare valid input data
model_params = [torch.randn(5), torch.randn(3)]
optimizer = torch.optim.SGD(model_params, lr=0.01, momentum=0.9)