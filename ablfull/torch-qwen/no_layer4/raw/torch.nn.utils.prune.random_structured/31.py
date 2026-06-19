import torch
import torch.nn as nn

# Step 1: Import PyTorch

# Step 2: Generate input data
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 5)

model = SimpleModel()
name = 'fc'
amount = 0.5
dim = 1

# Step 3: Call the API
pruned_model = nn.utils.prune.random_structured(model, name, amount, dim)