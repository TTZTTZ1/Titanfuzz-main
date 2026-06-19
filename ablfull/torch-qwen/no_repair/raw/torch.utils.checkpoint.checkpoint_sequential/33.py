import torch
from torch.nn import Sequential

# Define a simple model as a sequential container of layers
model = Sequential(
    torch.nn.Linear(10, 5),
    torch.nn.ReLU(),
    torch.nn.Linear(5, 2)
)

# Create some dummy input data
input_data = torch.randn(1, 10)

# Checkpoint the model sequentially
output = torch.utils.checkpoint.checkpoint_sequential(model, segments=2, input=input_data, use_reentrant=True)

print(output.shape)