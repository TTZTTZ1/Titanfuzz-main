import torch

# Initialize GRUCell
input_size = 10
hidden_size = 20
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Input and Hidden State
input_data = torch.randn(1, input_size)  # Batch size of 1
hidden_state = torch.randn(1, hidden_size)

# Forward pass
new_hidden_state = gru_cell(input_data, hidden_state)
print(new_hidden_state)