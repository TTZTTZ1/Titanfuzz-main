import torch

# Define model parameters
input_size = 10
hidden_size = 20

# Initialize GRUCell
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Create random input and hidden state
input_tensor = torch.randn(1, input_size)
hidden_state = torch.randn(1, hidden_size)

# Perform forward pass
new_hidden_state = gru_cell(input_tensor, hidden_state)

print(new_hidden_state)