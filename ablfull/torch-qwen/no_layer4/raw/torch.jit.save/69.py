import torch

# Prepare input data
m = torch.jit.script(torch.nn.Linear(10, 5))  # Example model
f = "model.pt"  # Path to save the model

# Call the API
torch.jit.save(m, f)