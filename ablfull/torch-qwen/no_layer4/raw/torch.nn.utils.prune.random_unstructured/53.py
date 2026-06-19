import torch
import torch.nn as nn

# Step 2: Generate input data
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(5, 3)

model = SimpleModel()

# Step 3: Call the API
torch.nn.utils.prune.random_unstructured(model.linear, name='weight', amount=0.5)