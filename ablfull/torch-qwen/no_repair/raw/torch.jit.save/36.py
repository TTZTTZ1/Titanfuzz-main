import torch

# Prepare valid input data
model = torch.jit.script(torch.nn.Linear(5, 2))  # Example model
file_path = 'example.pt'  # Example file path

# Call the API
torch.jit.save(model, file_path)