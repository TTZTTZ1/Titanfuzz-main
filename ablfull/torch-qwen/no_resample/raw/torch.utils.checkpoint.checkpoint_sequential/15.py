import torch
from torch import nn

# Task 2: Generate input data
input_tensor = torch.randn(1, 3, 224, 224)

# Define a simple sequential model for demonstration
model = nn.Sequential(
    nn.Conv2d(3, 64, kernel_size=3),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2),
    nn.Conv2d(64, 128, kernel_size=3),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2)
)

# Convert the model to a list of modules
functions_list = list(model.children())

# Number of segments for checkpointing
segments = 2

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(functions_list, segments, input_tensor, use_reentrant=True)