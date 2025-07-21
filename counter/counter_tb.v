module counter_tb;
    reg clk, reset, up_down;
    wire [3:0] count;

    reg [2:0] input_mem [0:9];  // 3 bits: clk, reset, up_down
    integer i;

    counter uut (.clk(clk), .reset(reset), .up_down(up_down), .count(count));

    initial clk = 0;
    always #5 clk = ~clk;  // clock toggles every 5 time units

    initial begin
        $readmemb("inputs.txt", input_mem); // read from fuzzed input
        $display("Time\tclk\treset\tup_down\tcount");

        for (i = 0; i < 10; i = i + 1) begin
            reset = input_mem[i][1];
            up_down = input_mem[i][0];
            #10; // let clock run
            $display("%0t\t%b\t%b\t%b\t%d", $time, clk, reset, up_down, count);
        end
        $finish;
    end
endmodule
