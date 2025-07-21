module mux_tb;
    reg [1:0] sel;
    reg [3:0] din;
    wire out;

    integer i;
    reg [5:0] input_mem [0:9];  // 6 bits: sel[1:0] + din[3:0]

    mux uut (.sel(sel), .din(din), .out(out));

    initial begin
        $readmemb("inputs.txt", input_mem); // Read fuzzed inputs
        $display("Time\tSel\tDin\tOut");
        for (i = 0; i < 10; i = i + 1) begin
            sel = input_mem[i][5:4];
            din = input_mem[i][3:0];
            #10;
            $display("%0t\t%b\t%b\t%b", $time, sel, din, out);
        end
        $finish;
    end
endmodule
