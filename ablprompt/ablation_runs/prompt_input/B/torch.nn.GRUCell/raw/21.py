import torch

# Initialize GRUCell
gru_cell = torch.nn.GRUCell(input_size=10, hidden_size=20)

# Create random input and hidden state
input_tensor = torch.randn(1, 10)
hidden_state = torch.randn(1, 20)

# Update hidden state
new_hidden_state = gru_cell(input_tensor, hidden_state)

print(new_hidden_state)