import torch
import torch.nn as nn
import torch.nn.utils.prune as prune

# Create a sample neural network module
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3)

model = SimpleNet()

# Prepare valid input data
name = 'conv1'
amount = 0.5  # Ensure this satisfies the constraint

# Call the API
pruned_model = prune.random_unstructured(model, name=name, amount=amount)