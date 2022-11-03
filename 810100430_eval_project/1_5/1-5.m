clc;
clear all;
close all;

%%  main function 

global zrng ;

zrng =[1,...
 1973272912, 281629770,  20006270,1280689831,2096730329,1933576050,...
  913566091, 246780520,1363774876, 604901985,1511192140,1259851944,...
  824064364, 150493284, 242708531,  75253171,1964472944,1202299975,...
  233217322,1911216000, 726370533, 403498145, 993232223,1103205531,...
  762430696,1922803170,1385516923,  76271663, 413682397, 726466604,...
  336157058,1432650381,1120463904, 595778810, 877722890,1046574445,...
   68911991,2088367019, 748545416, 622401386,2122378830, 640690903,...
 1774806513,2132545692,2079249579,  78130110, 852776735,1187867272,...
 1351423507,1645973084,1997049139, 922510944,2045512870, 898585771,...
  243649545,1004818771, 773686062, 403188473, 372279877,1901633463,...
  498067494,2087759558, 493157915, 597104727,1530940798,1814496276,...
  536444882,1663153658, 855503735,  67784357,1432404475, 619691088,...
  119025595, 880802310, 176192644,1116780070, 277854671,1366580350,...
 1142483975,2026948561,1053920743, 786262391,1792203830,1494667770,...
 1923011392,1433700034,1244184613,1147297105, 539712780,1545929719,...
  190641742,1645390429, 264907697, 620389253,1502074852, 927711160,...
  364849192,2049576050, 638580085, 547070247 ];

Q_LIMIT = 100 ; % Limit on queue length. 
BUSY  =    1  ;% Mnemonics for server's being busy 
IDLE  =    0 ; % and idle. 

global   next_event_type num_custs_delayed num_delays_required num_events num_policies  ;
global area_num_in_q area_server_status mean_interarrival mean_service sim_time time_last_event  avg_holding_cost avg_ordering_cost avg_shortage_cost;

global  time_arrival ;
time_arrival = zeros(Q_LIMIT + 1);

global time_next_event ;
time_next_event = zeros(1,5);


global amount bigs initial_inv_level inv_level   ;
global num_months num_values_demand smalls minlag mean_interdemand setup_cost ;
global area_holding area_shortage holding_cost incremental_cost maxlag ;
global shortage_cost  total_ordering_cost;

global prob_distrib_demand
prob_distrib_demand = zeros(1,26);
 



%%

% disp(sum(abs(matlab_symbols - symbols)));

% A1 = [9.9, 9900];
% A2 = [8.8,  7.7 ; ...
%       8800, 7700];
% formatSpec = 'X is %4.2f meters or %8.3f mm\n';
% fprintf(formatSpec,A1,A2)

% fid = fopen(filename, 'r');
% if fid == -1
% 		% fopen failed
% 
% else
% % fopen successful, okay to call fread
% A = fread(fid);


%  Open input and output files. 

infile = fopen('inv.in', 'r');
read_data_mm1_in = fread(infile);

%   Specify the number of events for the timing function. 

num_events = 4;

% /* Read input parameters. */
initial_inv_level = read_data_mm1_in(1);
num_months  = read_data_mm1_in(2);
num_policies  = read_data_mm1_in(3);

num_values_demand = read_data_mm1_in(4);
mean_interdemand = read_data_mm1_in(5);
setup_cost = read_data_mm1_in(6);
incremental_cost = read_data_mm1_in(7);
holding_cost = read_data_mm1_in(8);
shortage_cost = read_data_mm1_in(9);
minlag = read_data_mm1_in(10);
maxlag = read_data_mm1_in(11); 

outfile = fopen('inv.out', 'w');


% /* Write report heading and input parameters. */

fprintf(outfile, "Single-product inventory system\n\n");
fprintf(outfile, "Initial inventory level%24d items\n\n",initial_inv_level);
fprintf(outfile, "Number of demand sizes%25d\n\n", num_values_demand);
fprintf(outfile, "Distribution function of demand sizes ");


for i = 1:  num_values_demand
 fprintf(outfile, "%8.3f", prob_distrib_demand(i));
end

fprintf(outfile, "\n\nMean interdemand time%26.2f\n\n", mean_interdemand);
fprintf(outfile, "Delivery lag range%29.2f to%10.2f months\n\n", minlag,maxlag);
fprintf(outfile, "Length of the simulation%23d months\n\n", num_months);
fprintf(outfile, "K =%6.1f i =%6.1f h =%6.1f pi =%6.1f\n\n",setup_cost, incremental_cost, holding_cost, shortage_cost);
fprintf(outfile, "Number of policies%29d\n\n", num_policies);
fprintf(outfile, " Average Average");
fprintf(outfile, " Average Average\n");
fprintf(outfile, " Policy total cost ordering cost");
fprintf(outfile, " holding cost shortage cost");




function order_arrival
    %  /* Order arrival event function. */
    
    % /* Increment the inventory level by the amount ordered. */
    inv_level = inv_level + amount;
    
    % /* Since no order is now outstanding, eliminate the order-arrival event from
    % consideration. */
    time_next_event(1) = 1.0e+30;
    
    
    
end


function data_out_lcgrand = lcgrand (stream) 



    zi     = zrng(stream);
    lowprd = (zi & 65535) * MULT1;
    hi31   = bitsrl(zi , 16) * MULT1 + bitsrl(lowprd , 16);
    zi     = ((lowprd & 65535) - MODLUS) + (bitsll((hi31 & 32767) , 16)) + bitsrl(hi31 , 15);
    if (zi < 0)
        zi = zi + MODLUS;
    end
    
    lowprd = (zi & 65535) * MULT2;
    hi31   = bitsrl(zi , 16) * MULT2 + bitsrl(lowprd , 16);
    zi     = ((lowprd & 65535) - MODLUS) + (bitsll((hi31 & 32767) , 16)) + bitsrl(hi31 , 15);
    if (zi < 0) 
        zi = zi + MODLUS;
    end
    zrng(stream) = zi;
%     data_out_lcgrand =  (zi >> 7 | 1) / 16777216.0;
    data_out_lcgrand = or(bitsrl(zi,7) ,1)/ 16777216.0;
end
    


function lcgrandst(zset,stream)
%   /* Set the current zrng for stream "stream" to zset. */

    zrng(stream) = zset;
end


function data_out_lcgrandgt = lcgrandgt ( stream )
% /* Return the current zrng for stream "stream". */

    data_out_lcgrandgt =  zrng(stream);

end



function initialize 

    % /* Initialize the simulation clock. */
    sim_time = 0.0;
    
    % /* Initialize the state variables. */
    inv_level = initial_inv_level;
    time_last_event = 0.0;
    
    % /* Initialize the statistical counters. */
    total_ordering_cost = 0.0;
    area_holding = 0.0;
    area_shortage = 0.0;
    
    % /* Initialize the event list. Since no order is outstanding, the orderarrival
    % event is eliminated from consideration. */
    time_next_event(1) = 1.0e+30;
    time_next_event(2) = sim_time + expon(mean_interdemand);
    time_next_event(3) = num_months;
    time_next_event(4) = 0.0;
    
end


function data_out_expon = expon (data_in_expon)

    %    /* Exponential variate generation function. */
        
    %     /* Return an exponential random variate with mean "mean". */
    
        data_out_expon =  ((-1)*data_in_expon) * log10(lcgrand(1));
end



function  evaluate


    if (inv_level < smalls) 
     
        amount = bigs - inv_level;
    
        total_ordering_cost = total_ordering_cost + setup_cost + incremental_cost * amount;
    
        % /* Schedule the arrival of the order. */
        time_next_event[0] = sim_time + uniform(minlag, maxlag);
    end
    % /* Regardless of the place-order decision, schedule the next inventory
    % evaluation. */
    
    time_next_event[3] = sim_time + 1.0;
    
    
end


function i = random_integer(prob_distrib)


    %  /* Random integer generationfunction. */
     
    % /* Generate a U(0,1) random variate. */
    u = lcgrand(1);
    
    
    % /* Return a random integer in accordance with the (cumulative) distribution
    % function prob_distrib. */
    
    
    i= 1 ;
        while(u >= prob_distrib(i))
    
           i = i+1 ; 
    
        end
    
    
    
end


function report
    %   /* Report generator function. */
    % /* Compute and write estimates of desired measures of performance. */
    avg_ordering_cost = total_ordering_cost / num_months;
    avg_holding_cost = holding_cost * area_holding / num_months;
    avg_shortage_cost = shortage_cost * area_shortage / num_months;
    
    fprintf(outfile, "\n\n(%3d,%3d)%15.2f%15.2f%15.2f%15.2f",smalls, bigs,avg_ordering_cost + avg_holding_cost + avg_shortage_cost,avg_ordering_cost, avg_holding_cost, avg_shortage_cost);
    
        
end


function  data_out_uniform = uniform( a , b )

    %  /* Uniform variate generation function. */
    
    % /* Return a U(a,b) random variate. */
    data_out_uniform =  a + lcgrand(1) * (b - a);
    
    
end
    
function  update_time_avg_stats

    % /* Update area accumulators for time-average statistics. */
    
    % /* Compute time since last event, and update last-event-time marker. */
    time_since_last_event = sim_time - time_last_event;
    time_last_event = sim_time;
    
    % /* Determine the status of the inventory level during the previous interval.
    % If the inventory level during the previous interval was negative, update
    % area_shortage. If it was positive, update area_holding. If it was zero,
    % no update is needed. */
    
        if (inv_level < 0)
            area_shortage = area_shortage - inv_level * time_since_last_event;
            
        elseif (inv_level > 0)
            area_holding = area_holding + inv_level * time_since_last_event;
    
        
        end
        
        
end

function demand
    %  /* Demand event function. */
    
    % /* Decrement the inventory level by a generated demand size. */
    inv_level = inv_level - random_integer(prob_distrib_demand);
    
    
    % /* Schedule the time of the next demand. */
    time_next_event(2) = sim_time + expon(mean_interdemand);
    
    
end



% /* Run the simulation varying the inventory policy. */
for i = 1: num_policies
    % /* Read the inventory policy, and initialize the simulation. */
    fscanf(infile, "%d %d", &smalls, &bigs);
    
    initialize();
    % /* Run the simulation until it terminates after an end-simulation event
    % (type 3) occurs. */

    while (next_event_type ~= 3)

    % /* Determine the next event. */
    timing();
    % /* Update time-average statistical accumulators. */
    update_time_avg_stats();
    % /* Invoke the appropriate event function. */



            switch (next_event_type) 
                case 1
                    order_arrival();
                    break;
                case 2
                    demand();
                    break;
                case 4
                    evaluate();
                    break;
                case 3
                    report();
                    break;
            end
    % /* If the event just executed was not the end-simulation event (type 3),
    % continue simulating. Otherwise, end the simulation for the current
    % (s,S) pair and go on to the next pair (if any). */
    end
end
% /* End the simulations. */
fclose(infile);
fclose(outfile);
