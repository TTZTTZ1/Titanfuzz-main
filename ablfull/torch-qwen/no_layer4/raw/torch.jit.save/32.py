import torch

# Define a simple model
model = torch.nn.Linear(10, 5)

# Prepare a file path
file_path = 'model.pt'

# Save the model
torch.jit.save(model, file_path)