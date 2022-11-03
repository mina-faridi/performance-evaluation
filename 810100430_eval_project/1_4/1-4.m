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

global   next_event_type num_custs_delayed num_delays_required num_events  ;
global area_num_in_q area_server_status mean_interarrival mean_service sim_time time_last_event ;

global  time_arrival ;
time_arrival = zeros(Q_LIMIT + 1);

global time_next_event ;
time_next_event = zeros(1,3);


global MODLUS 
 MODLUS = 2147483647 ;
 
 
global MULT1 MULT2 
MULT1  = 24112 ;
MULT2  = 26143 ;

function update_time_avg_stats
    time_since_last_event = sim_time - time_last_event;
    time_last_event       = sim_time;
    area_num_in_q      = area_num_in_q + (num_in_q * time_since_last_event);
    area_server_status = area_server_status + (server_status * time_since_last_event);
end

function timing
    int   i;
    float min_time_next_event = 1.0e+29;
    next_event_type = 0;
    for i = 1: num_events
        if (time_next_event(i) < min_time_next_event)
            min_time_next_event = time_next_event(i);
            next_event_type     = i;
        end
    end
    if (next_event_type == 0)
        fprintf(outfile, "\nEvent list empty at time %f", sim_time);
        exit(1);
    end
    sim_time = min_time_next_event;
    end

    function report
    fprintf(outfile, "\n\nAverage delay in queue%11.3f minutes\n\n",total_of_delays / num_custs_delayed);
    fprintf(outfile, "Average number in queue%10.3f\n\n",area_num_in_q / sim_time);
    fprintf(outfile, "Server utilization%15.3f\n\n",area_server_status / sim_time);
    fprintf(outfile, "Time simulation ended%12.3f minutes", sim_time);
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
    zrng(stream) = zset;
end


function data_out_lcgrandgt = lcgrandgt ( stream )
    data_out_lcgrandgt =  zrng(stream);
end


function initialize 
    sim_time = 0.0;
    server_status   = IDLE;
    num_in_q        = 0;
    time_last_event = 0.0;
    num_custs_delayed  = 0;
    total_of_delays    = 0.0;
    area_num_in_q      = 0.0;
    area_server_status = 0.0;
    time_next_event(2) = sim_time + expon(mean_interarrival);
    time_next_event(3) = 1.0e+30;
end

function depart
    if (num_in_q == 0)
        server_status      = IDLE;
        time_next_event[2] = 1.0e+30;
    else
        num_in_q = num_in_q -1 ;
        delay            = sim_time - time_arrival[1];
        total_of_delays = total_of_delays + delay;

        num_custs_delayed = num_custs_delayed +1 ;
        time_next_event(3) = sim_time + expon(mean_service);

        for i = 1: num_in_q
            time_arrival(i) = time_arrival(i + 1);
        end
    end
    
end


function arrive
    time_next_event(2) = sim_time + expon(mean_interarrival);
    if (server_status == BUSY)
        num_in_q = num_in_q + 1 ;
        if (num_in_q > Q_LIMIT)
            fprintf(outfile, "\nOverflow of the array time_arrival at");
            fprintf(outfile, " time %f", sim_time);
            exit(1);
        end
        time_arrival(num_in_q) = sim_time;
    else
        delay            = 0.0;
        total_of_delays += delay;
        num_custs_delayed = num_custs_delayed + 1;
        server_status = BUSY;
        time_next_event(3) = sim_time + expon(mean_service);
    end
end


function data_out_expon = expon (data_in_expon)
    data_out_expon =  ((-1)*data_in_expon) * log10(lcgrand(1));
end

clc;
clear all;
close all;


%%  main function 




infile = fopen('mm1alt.in', 'r');
read_data_mm1_in = fread(infile);
num_events = 3;

% /* Read input parameters. */
mean_interarrival = read_data_mm1_in(1);
mean_service  = read_data_mm1_in(2);
num_delays_required  = read_data_mm1_in(3);

outfile = fopen('mm1alt.out', 'w');


% /* Write report heading and input parameters. */

fprintf(outfile, "Single-server queueing system\n\n");
fprintf(outfile, "Mean interarrival time%11.3f minutes\n\n", mean_interarrival);
fprintf(outfile, "Mean service time%16.3f minutes\n\n", mean_service);
fprintf(outfile, "Number of customers%14d\n\n", num_delays_required);

next_event_type = 0  ;

% /* Initialize the simulation. */

    initialize();

%     /* Run the simulation while more delays are still needed. */

    while (next_event_type ~= 3)     
    
%         /* Determine the next event. */

        timing();

%         /* Update time-average statistical accumulators. */

        update_time_avg_stats();

%         /* Invoke the appropriate event function. */

        switch (next_event_type) 
        
            case 1
                arrive();
                break;
            case 2
                depart();
                break;
        end
        
    end
    

%     /* Invoke the report generator and end the simulation. */

    report();

    fclose(infile);
    fclose(outfile);
