import torch

# Generate valid input data
input_1 = torch.tensor([0.5, -0.5])
input_2 = torch.tensor([-0.2, 0.3])
target = torch.tensor([1, -1])

# Call the API with valid parameters
loss_fn = torch.nn.HingeEmbeddingLoss(margin=1.0, reduction='mean')
loss = loss_fn(input_1, input_2, target)
print(loss)