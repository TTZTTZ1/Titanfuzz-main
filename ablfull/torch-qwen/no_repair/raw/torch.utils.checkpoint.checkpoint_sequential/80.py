import torch
import torch.nn as nn

# Task 2: Generate input data
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(10, 5)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(5, 1)

model = SimpleModel().eval()

input_tensor = torch.randn(4, 10)

# Task 3: Call the API
output = torch.utils.checkpoint.checkpoint_sequential(
    model.children(),
    segments=2,
    input=input_tensor,
    use_reentrant=False
)