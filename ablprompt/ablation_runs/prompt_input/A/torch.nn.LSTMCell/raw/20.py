import torch

# Initialize LSTMCell
input_size = 10
hidden_size = 20
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Input and Hidden State Initialization
input_data = torch.randn(1, input_size)  # batch_size=1, input_size=10
hidden_state = torch.randn(1, hidden_size)
cell_state = torch.randn(1, hidden_size)

# Forward Pass
new_hidden_state, new_cell_state = lstm_cell(input_data, (hidden_state, cell_state))

print("New Hidden State:", new_hidden_state)
print("New Cell State:", new_cell_state)