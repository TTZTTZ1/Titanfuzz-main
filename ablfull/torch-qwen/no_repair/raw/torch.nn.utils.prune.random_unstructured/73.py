import torch
import torch.nn as nn

# Step 1: Create a simple model to prune
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 5)

model = SimpleModel()

# Step 2: Prepare input data for pruning
name_to_prune = 'fc.weight'
amount_to_prune = 0.2

# Step 3: Call the API
torch.nn.utils.prune.random_unstructured(model, name=name_to_prune, amount=amount_to_prune)