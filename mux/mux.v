module mux (
    input [1:0] sel,
    input [3:0] din,
    output reg out
);
    always @(*) begin
        case (sel)
            2'b00: out = din[0];
            2'b01: out = din[1];
            2'b10: out = din[2];
            2'b11: out = din[3];
        endcase
    end
endmodule
