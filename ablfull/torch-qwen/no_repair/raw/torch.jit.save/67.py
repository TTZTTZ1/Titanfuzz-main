import torch

# Create a simple model
model = torch.nn.Sequential(torch.nn.Linear(4, 5), torch.nn.ReLU(), torch.nn.Linear(5, 2))

# Define a file path to save the model
file_path = 'model.pt'

# Save the model
torch.jit.save(model, file_path)