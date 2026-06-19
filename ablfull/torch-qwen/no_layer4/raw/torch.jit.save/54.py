import torch

# Prepare valid input data
m = torch.jit.script(torch.nn.Linear(10, 5))
f = "model.pt"

# Call the API
torch.jit.save(m, f)