import torch

# Step 2: Prepare valid input data
m = torch.jit.script(torch.nn.Linear(10, 5))
f = "model.pt"

# Step 3: Call the API
torch.jit.save(m, f)