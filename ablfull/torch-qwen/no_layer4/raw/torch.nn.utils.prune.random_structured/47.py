import torch
from torch.nn.utils import prune

# Create a sample convolutional neural network module
class SimpleCNN(torch.nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = torch.nn.Conv2d(1, 64, kernel_size=3)
    
    def forward(self, x):
        return self.conv1(x)

model = SimpleCNN()

# Define the parameters for random_structured pruning
name = 'conv1.weight'
amount = 0.5
dim = 0

# Apply random_structured pruning to the model's named parameter
prune.random_structured(model, name, amount=amount, dim=dim)