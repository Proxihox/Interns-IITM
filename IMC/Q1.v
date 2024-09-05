module first_common_element (
    input logic [3:0] a,  // First 4-bit input
    input logic [3:0] b,  // Second 4-bit input
    output logic out 
);
    always_comb begin
        out = 1'b0
        for (int i = 0; i < 4; i++) begin
            if(a[i] == b[i]) begin
                out = a[i]
            end
        end
