import torch
import torch.nn as nn

# Create a sample model
class SampleModel(nn.Module):
    def __init__(self):
        super(SampleModel, self).__init__()
        self.conv = nn.Conv2d(1, 64, kernel_size=3)

model = SampleModel()

# Define input parameters
name = 'conv'
amount = 0.5

# Apply random unstructured pruning
torch.nn.utils.prune.random_unstructured(model, name=name, amount=amount)