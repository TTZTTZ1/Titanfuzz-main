import torch

# Define a simple script module
script_module = torch.jit.script(torch.nn.Linear(10, 5))

# Save the script module to a file
torch.jit.save(script_module, "model.pt")