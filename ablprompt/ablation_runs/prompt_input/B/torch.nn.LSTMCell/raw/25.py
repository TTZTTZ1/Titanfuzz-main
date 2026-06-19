import torch

# Define model parameters
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Input sequence and initial hidden/cell states
batch_size = 5
sequence_length = 3
input_sequence = torch.randn(sequence_length, batch_size, input_size)
h0 = torch.zeros(batch_size, hidden_size)
c0 = torch.zeros(batch_size, hidden_size)

# Process sequence through LSTMCell
outputs = []
hn = h0
cn = c0
for t in range(sequence_length):
    ht, ct = lstm_cell(input_sequence[t], (hn, cn))
    outputs.append(ht)
    hn = ht
    cn = ct

# Stack outputs
final_outputs = torch.stack(outputs, dim=0)
print(final_outputs.shape)  # Should print: torch.Size([3, 5, 20])