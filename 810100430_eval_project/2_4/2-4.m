clc;
clear all;
close all;


%%  main function 


global EVENT_ARRIVAL EVENT_DEPARTURE LIST_QUEUE LIST_SERVER SAMPST_DELAYS STREAM_INTERARRIVAL STREAM_SERVICE ;

EVENT_ARRIVAL =  1 ;%;/* Event type for arrival. */
 EVENT_DEPARTURE= 2; %/* Event type for departure. */
 LIST_QUEUE= 1 ;%;/* List number for queue. */
 LIST_SERVER= 2 ;%/* List number for server. */
 SAMPST_DELAYS =1 ;%/* sampst variable for delays in queue. */
 STREAM_INTERARRIVAL= 1; %/* Random-number stream for interarrivals. */
 STREAM_SERVICE =2; %/* Random-number stream for service times. */
 
 
% /* Declare non-simlib global variables. */
global  num_custs_delayed num_delays_required;
global mean_interarrival mean_service;


infile = fopen('mm1smlb.in', 'r');
read_data_in = fread(infile);

outfile = fopen('mm1smlb.out', 'w');

% /* Read input parameters. */
mean_interarrival = read_data_in(1);
mean_service  = read_data_in(2);
num_delays_required  = read_data_in(3);





% /* Write report heading and input parameters. */
fprintf(outfile, "Single-server queueing system using simlib\n\n");
fprintf(outfile, "Mean interarrival time%11.3f minutes\n\n",mean_interarrival);
fprintf(outfile, "Mean service time%16.3f minutes\n\n", mean_service);
fprintf(outfile, "Number of customers%14d\n\n\n", num_delays_required);

% /* Initialize simlib */
init_simlib();

% /* Set maxatr = max(maximum number of attributes per record, 4) */
maxatr = 4; %/* NEVER SET maxatr TO BE SMALLER THAN 4. */



function arrive


    % /* Schedule next arrival. */
    event_schedule(sim_time + expon(mean_interarrival, STREAM_INTERARRIVAL),EVENT_ARRIVAL);
    
        % /* Check to see whether server is busy (i.e., list SERVER contains arecord). */
        if (list_size(LIST_SERVER) == 1) 
    
            % /* Server is busy, so store time of arrival of arriving customer at end
            % of list LIST_QUEUE. */
            transfer(1) = sim_time;
            list_file(LAST, LIST_QUEUE);
    
        else 
    %          /* Server is idle, so start service on arriving customer, who has a
    %         delay of zero. (The following statement IS necessary here.) */
            sampst(0.0, SAMPST_DELAYS);
            % /* Increment the number of customers delayed. */
            num_custs_delayed = num_custs_delayed +1 ;
            % /* Make server busy by filing a dummy record in list LIST_SERVER. */
            list_file(FIRST, LIST_SERVER);
            % /* Schedule a departure (service completion). */
            event_schedule(sim_time + expon(mean_service, STREAM_SERVICE),EVENT_DEPARTURE);
    
        end
    
end

function depart
 
% /* Check to see whether queue is empty. */
    if (list_size(LIST_QUEUE) == 0)
        % /* The queue is empty, so make the server idle and leave the departure
        % (service completion) event out of the event list. (It is currently
        % not in the event list, having just been removed by timing before
        % coming here.) */
        list_remove(FIRST, LIST_SERVER);
    else 
        % /* The queue is nonempty, so remove the first customer from the queue,
        % register delay, increment the number of customers delayed, and
        % schedule departure. */
        list_remove(FIRST, LIST_QUEUE);
        sampst(sim_time - transfer(1), SAMPST_DELAYS);
        num_custs_delayed = num_custs_delayed + 1 ;
        event_schedule(sim_time + expon(mean_service, STREAM_SERVICE),EVENT_DEPARTURE);
    
    end
        
end

function data_out_expon = expon (data_in_expon)

    %    /* Exponential variate generation function. */
     
    %     /* Return an exponential random variate with mean "mean". */
    
        data_out_expon =  ((-1)*data_in_expon) * log10(lcgrand(1));
end

function init_model


    %  /* Initialization function. */

    num_custs_delayed = 0;

    event_schedule(sim_time + expon(mean_interarrival, STREAM_INTERARRIVAL),EVENT_ARRIVAL);


end

function report

 
    % /* Get and write out estimates of desired measures of performance. */
    fprintf(outfile, "\nDelays in queue, in minutes:\n");
    
    out_sampst(outfile, SAMPST_DELAYS, SAMPST_DELAYS);
    
    fprintf(outfile, "\nQueue length (1) and server utilization (2):\n");
    
    out_filest(outfile, LIST_QUEUE, LIST_SERVER);
    
    fprintf(outfile, "\nTime simulation ended:%12.3f minutes\n", sim_time);
    
    
end   


% /* Initialize the model. */
init_model();
% /* Run the simulation while more delays are still needed. */
while (num_custs_delayed < num_delays_required) 
% /* Determine the next event. */

timing();

% /* Invoke the appropriate event function. */

        switch (next_event_type) 
            case EVENT_ARRIVAL:
                arrive();
                 break;
            case EVENT_DEPARTURE:
                depart();
                 break;
        end
end
% /* Invoke the report generator and end the simulation. */
report();


fclose(infile);
fclose(outfile);



    