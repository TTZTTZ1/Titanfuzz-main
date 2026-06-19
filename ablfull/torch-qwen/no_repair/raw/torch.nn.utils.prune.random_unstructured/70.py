import torch.nn as nn
import torch.nn.utils.prune

# Define a simple model for demonstration
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(10, 5)

model = SimpleModel()

# Prepare valid input data
module = model.linear
name = 'weight'
amount = 0.3

# Call the API
pruned_module = prune.random_unstructured(module, name=name, amount=amount)