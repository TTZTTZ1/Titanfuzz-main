import torch
import torch.nn as nn

# Define a sample model
class SampleModel(nn.Module):
    def __init__(self):
        super(SampleModel, self).__init__()
        self.conv = nn.Conv2d(1, 1, kernel_size=3)

model = SampleModel()

# Prepare input data
amount = 0.5

# Call the API
torch.nn.utils.prune.random_unstructured(model.conv, name="weight", amount=amount)