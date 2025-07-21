module alu (
    input [3:0] A,
    input [3:0] B,
    input [2:0] opcode,
    output reg [3:0] result
);
    always @(*) begin
        case (opcode)
            3'b000: result = A + B;
            3'b001: result = A - B;
            3'b010: result = A & B;
            3'b011: result = A | B;
            3'b100: result = A ^ B;
            3'b101: result = ~A;
            default: result = 4'b0000;
        endcase
    end
endmodule
