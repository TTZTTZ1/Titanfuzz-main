import torch

# Create a simple model
model = torch.nn.Sequential(
    torch.nn.Linear(10, 5),
    torch.nn.ReLU(),
    torch.nn.Linear(5, 2)
)

# Define the file path to save the model
file_path = 'simple_model.pt'

# Save the model using torch.jit.save
torch.jit.save(model, file_path)