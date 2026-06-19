import torch
import torch.nn as nn

# Step 2: Generate input data
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv = nn.Conv2d(1, 1, kernel_size=3)

model = SimpleModel()
name = 'conv'
amount = 0.5

# Step 3: Call the API
torch.nn.utils.prune.random_unstructured(model, name=name, amount=amount)