import torch

# Prepare valid input data
class SimpleModule(torch.nn.Module):
    def __init__(self):
        super(SimpleModule, self).__init__()
        self.linear1 = torch.nn.Linear(10, 10)
        self.linear2 = torch.nn.Linear(10, 10)

    def forward(self, x):
        return self.linear2(self.linear1(x))

functions = SimpleModule()
segments = 2
input_tensor = torch.randn(5, 10)

# Call the API
result = torch.utils.checkpoint.checkpoint_sequential(
    [functions], segments, input_tensor, use_reentrant=False
)