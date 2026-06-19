
import torch

class SimpleLayer(torch.nn.Module):

    def forward(self, x):
        return (x * 2)
model = torch.nn.Sequential(SimpleLayer(), SimpleLayer())
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
result = torch.utils.checkpoint.checkpoint_sequential(model, segments=1, input=input_tensor, use_reentrant=True)
print(result)
