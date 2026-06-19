import torch

# Create a simple script module
m = torch.jit.script(torch.nn.Linear(10, 1))

# Define the file path for saving the model
f = "model.pt"

# Save the model
torch.jit.save(m, f)