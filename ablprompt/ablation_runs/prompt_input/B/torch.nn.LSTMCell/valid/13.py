import torch

# Initialize LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size=10, hidden_size=20)

# Input sequence of length 5
input_sequence = torch.randn(5, 1, 10)

# Initial hidden and cell states
h0 = torch.zeros(1, 20)
c0 = torch.zeros(1, 20)

# Process each time step
outputs = []
for input_t in input_sequence:
    h0, c0 = lstm_cell(input_t, (h0, c0))
    outputs.append(h0)

# Stack outputs
final_output = torch.stack(outputs)
print(final_output.shape)  # Should print: torch.Size([5, 1, 20])