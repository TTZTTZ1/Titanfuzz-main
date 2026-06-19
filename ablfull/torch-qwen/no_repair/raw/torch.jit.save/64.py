import torch

# Step 2: Generate input data
model = torch.nn.Linear(10, 5)
filename = 'model.pt'

# Step 3: Call the API
torch.jit.save(model, filename)