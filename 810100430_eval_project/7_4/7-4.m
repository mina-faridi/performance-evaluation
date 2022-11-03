%{
clc;
clear all;
close all;

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

global MODLUS 
 MODLUS = 2147483647 ;
 
 
global MULT1 MULT2 
MULT1  = 24112 ;
MULT2  = 26143 ;

   %}


clc;
clear all;
close all;

%%  main function


global drng ;
drng =[ 0, 0, 1, 0, 0, 1;
1772212344, 1374954571, 2377447708, 540628578, 1843308759, 549575061;
2602294560, 1764491502, 3872775590, 4089362440, 2683806282, 437563332;
376810349, 1545165407, 3443838735, 3650079346, 1898051052, 2606578666;
1847817841, 3038743716, 2014183350, 2883836363, 3242147124, 1955620878;
1075987441, 3468627582, 2694529948, 368150488, 2026479331, 2067041056;
134547324, 4246812979, 1700384422, 2358888058, 83616724, 3045736624;
2816844169, 885735878, 1824365395, 2629582008, 3405363962, 1835381773;
675808621, 434584068, 4021752986, 3831444678, 4193349505, 2833414845;
2876117643, 1466108979, 163986545, 1530526354, 68578399, 1111539974;
411040508, 544377427, 2887694751, 702892456, 758163486, 2462939166;
3631741414, 3388407961, 1205439229, 581001230, 3728119407, 94602786;
4267066799, 3221182590, 2432930550, 813784585, 1980232156, 2376040999;
1601564418, 2988901653, 4114588926, 2447029331, 4071707675, 3696447685;
3878417653, 2549122180, 1351098226, 3888036970, 1344540382, 2430069028;
197118588, 1885407936, 576504243, 439732583, 103559440, 3361573194;
4024454184, 2530169746, 2135879297, 2516366026, 260078159, 2905856966;
2331743881, 2059737664, 186644977, 401315249, 72328980, 1082588425;
694808921, 2851138195, 1756125381, 1738505503, 2662188364, 3598740668;
2834735415, 2017577369, 3257393066, 3823680297, 2315410613, 637316697;
4132025555, 3700940887, 838767760, 2818574268, 1375004287, 2172829019;
560024289, 1830276631, 144885590, 1556615741, 1597610225, 1856413969;
1031792556, 1844191084, 1441357589, 3147919604, 199001354, 2555043119;
2023049680, 4184669824, 4074523931, 252765086, 3328098427, 1480103038];

drng = drng' ;




global norm  norm2 m1 m2 ;
norm  = 2.328306549295728e-10 ;%/* 1.0/(m1+1) */
norm2  = 2.328318825240738e-10 ;% /* 1.0/(m2+1) */ 
m1  = 4294967087.0 ;
m2  = 4294944443.0 ;



% /* Set the default seeds for all 100 streams. */



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


function data_out_expon = expon (data_in_expon)

    %    /* Exponential variate generation function. */
     
    %     /* Return an exponential random variate with mean "mean". */
    
        data_out_expon =  ((-1)*data_in_expon) * log10(lcgrand(1));
end


function mradst( seed,  stream)


    for i = 0: 5 
        drng(stream,i+1) = seed(i+1);

    end


end

    
function data_out_mrand = mrand(stream)


    s10 = drng(stream,1);
    s11 = drng(stream,2);
    s12 = drng(stream,3);
    
    s20 = drng(stream,4);
    s21 = drng(stream,5);
    s22 = drng(stream,6);
    
    
    p = 1403580.0 * s11 - 810728.0 * s10;
    
    k = p / m1;
    p = p - k*m1;
    
    if (p < 0.0)
        p = p + m1;
    end
    
    s10 = s11;
    s11 = s12; 
    s12 = p;
    
    p = 527612.0 * s22 - 1370589.0 * s20;
    
    k = p / m2;
    p = p - k*m2;
    
    if (p < 0.0)
        p = p + m2;
    end
    
    s20 = s21;
    s21 = s22; 
    s22 = p;
    
    drng(stream,0) = s10; 
    drng(stream,1) = s11;
    drng(stream,2) = s12;
    drng(stream,3) = s20;
    drng(stream,4) = s21;
    drng(stream,5) = s22;
    
    if (s12 <= s22) 
        data_out_mrand  =  ((s12 - s22 + m1) * norm);
    else
        data_out_mrand  = (s12 - s22) * norm);
    end
    
end

function   mrandgt( seed,  stream)



    for i = 0: 5
        seed(i+1) = drng(stream,i+1);

    end


end





