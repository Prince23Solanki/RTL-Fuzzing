module fsm_tb;
    reg clk, reset, din;
    wire out;

    reg [1:0] input_mem [0:9]; // 2-bit per cycle: reset, din
    integer i;

    fsm uut (.clk(clk), .reset(reset), .din(din), .out(out));

    initial clk = 0;
    always #5 clk = ~clk; // Clock toggles every 5 units

    initial begin
        $readmemb("inputs.txt", input_mem);
        $display("Time\tclk\treset\tdin\tout");

        for (i = 0; i < 10; i = i + 1) begin
            reset = input_mem[i][1];
            din = input_mem[i][0];
            #10;
            $display("%0t\t%b\t%b\t%b\t%b", $time, clk, reset, din, out);
        end
        $finish;
    end
endmodule
