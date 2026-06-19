
import torch
model = torch.nn.Sequential(torch.nn.Linear(10, 5), torch.nn.ReLU(), torch.nn.Linear(5, 2))
input_tensor = torch.randn(1, 10)
result = torch.utils.checkpoint.checkpoint_sequential(model, 1, input_tensor, use_reentrant=True)
