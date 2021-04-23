from Formula_Parser import FormulaParser as fParser


def pipline(text):
    fp = fParser()
    formula = text
    fp.ReadFormula(formula)
    fp.Tokenize()
    fp.OpenBracket()
    fp.Translate()
    return fp.output

print('=========C1 is not avaliable===')
print('=========C2 ====')
print(pipline('(v[2534])-1*(v[2533])+1*(v[2514] - pow(v[2535], 2))'))
print('=========C3 ====')
print(pipline('(v[2532])-3*(v[2531])+3*(-v[2535]*v[2534] + v[2469])+2*(v[2530])-3*(-v[2535]*v[2533] + v[2468])+1*(-3*v[2514]*v[2535] + v[2513] + 2*pow(v[2535], 3))'))
print('=========C4 ====')
print(pipline('(v[2529])-7*(v[2528])+4*(-v[2535]*v[2532] + v[2467])+3*(v[2506] - pow(v[2534], 2))+12*(v[2527])-12*(-v[2535]*v[2531] + v[2466])-6*(-v[2534]*v[2533] + v[2449])+6*(-v[2514]*v[2534] + 2*pow(v[2535], 2)*v[2534] - 2*v[2535]*v[2469] + v[2259])-6*(v[2526])+8*(-v[2535]*v[2530] + v[2465])+3*(v[2501] - pow(v[2533], 2))-6*(-v[2514]*v[2533] + 2*pow(v[2535], 2)*v[2533] - 2*v[2535]*v[2468] + v[2258])+1*(-3*pow(v[2514], 2) + 12*v[2514]*pow(v[2535], 2) - 4*v[2513]*v[2535] + v[2512] - 6*pow(v[2535], 4))'))
print('=========C5 ====')
print(pipline('(v[2525])-15*(v[2524])+5*(-v[2535]*v[2529] + v[2464])+10*(-v[2534]*v[2532] + v[2448])+50*(v[2523])-35*(-v[2535]*v[2528] + v[2463])-10*(-v[2533]*v[2532] + v[2430])+10*(-v[2514]*v[2532] + 2*pow(v[2535], 2)*v[2532] - 2*v[2535]*v[2467] + v[2257])-30*(-v[2534]*v[2531] + v[2447])+15*(-v[2535]*v[2506] + 2*v[2535]*pow(v[2534], 2) + v[2131] - 2*v[2534]*v[2469])-60*(v[2522])+60*(-v[2535]*v[2527] + v[2462])+30*(-v[2533]*v[2531] + v[2429])-30*(-v[2514]*v[2531] + 2*pow(v[2535], 2)*v[2531] - 2*v[2535]*v[2466] + v[2256])+20*(-v[2534]*v[2530] + v[2446])-30*(2*v[2535]*v[2534]*v[2533] - v[2535]*v[2449] - v[2534]*v[2468] - v[2469]*v[2533] + v[1836])+10*(6*v[2514]*v[2535]*v[2534] - 3*v[2514]*v[2469] - v[2513]*v[2534] - 6*pow(v[2535], 3)*v[2534] + 6*pow(v[2535], 2)*v[2469] - 3*v[2535]*v[2259] + v[2239])+24*(v[2521])-30*(-v[2535]*v[2526] + v[2461])-20*(-v[2533]*v[2530] + v[2428])+20*(-v[2514]*v[2530] + 2*pow(v[2535], 2)*v[2530] - 2*v[2535]*v[2465] + v[2255])+15*(-v[2535]*v[2501] + 2*v[2535]*pow(v[2533], 2) + v[2127] - 2*v[2533]*v[2468])-10*(6*v[2514]*v[2535]*v[2533] - 3*v[2514]*v[2468] - v[2513]*v[2533] - 6*pow(v[2535], 3)*v[2533] + 6*pow(v[2535], 2)*v[2468] - 3*v[2535]*v[2258] + v[2238])+1*(30*pow(v[2514], 2)*v[2535] - 10*v[2514]*v[2513] - 60*v[2514]*pow(v[2535], 3) + 20*v[2513]*pow(v[2535], 2) - 5*v[2512]*v[2535] + v[2511] + 24*pow(v[2535], 5))'))
print('=========C6 ====')
print(pipline('(v[2520])-31*(v[2519])+6*(-v[2535]*v[2525] + v[2460])+15*(-v[2534]*v[2529] + v[2445])+180*(v[2518])-90*(-v[2535]*v[2524] + v[2459])-15*(-v[2533]*v[2529] + v[2427])+15*(-v[2514]*v[2529] + 2*pow(v[2535], 2)*v[2529] - 2*v[2535]*v[2464] + v[2254])+10*(v[2496] - pow(v[2532], 2))-105*(-v[2534]*v[2528] + v[2444])-60*(-v[2532]*v[2531] + v[2412])+60*(2*v[2535]*v[2534]*v[2532] - v[2535]*v[2448] - v[2534]*v[2467] - v[2469]*v[2532] + v[1835])-390*(v[2517])+300*(-v[2535]*v[2523] + v[2458])+105*(-v[2533]*v[2528] + v[2426])-105*(-v[2514]*v[2528] + 2*pow(v[2535], 2)*v[2528] - 2*v[2535]*v[2463] + v[2253])+40*(-v[2532]*v[2530] + v[2411])-60*(2*v[2535]*v[2533]*v[2532] - v[2535]*v[2430] - v[2533]*v[2467] - v[2468]*v[2532] + v[1817])+20*(6*v[2514]*v[2535]*v[2532] - 3*v[2514]*v[2467] - v[2513]*v[2532] - 6*pow(v[2535], 3)*v[2532] + 6*pow(v[2535], 2)*v[2467] - 3*v[2535]*v[2257] + v[2237])+15*(-3*v[2506]*v[2534] + v[2505] + 2*pow(v[2534], 3))+180*(-v[2534]*v[2527] + v[2443])+90*(v[2493] - pow(v[2531], 2))-180*(2*v[2535]*v[2534]*v[2531] - v[2535]*v[2447] - v[2534]*v[2466] - v[2469]*v[2531] + v[1834])-45*(-v[2506]*v[2533] + 2*pow(v[2534], 2)*v[2533] - 2*v[2534]*v[2449] + v[2108])+45*(-v[2514]*v[2506] + 2*v[2514]*pow(v[2534], 2) + 2*pow(v[2535], 2)*v[2506] - 6*pow(v[2535], 2)*pow(v[2534], 2) - 2*v[2535]*v[2131] + 8*v[2535]*v[2534]*v[2469] + v[1935] - 2*v[2534]*v[2259] - 2*pow(v[2469], 2))+360*(v[2516])-360*(-v[2535]*v[2522] + v[2457])-180*(-v[2533]*v[2527] + v[2425])+180*(-v[2514]*v[2527] + 2*pow(v[2535], 2)*v[2527] - 2*v[2535]*v[2462] + v[2252])-120*(-v[2531]*v[2530] + v[2395])+180*(2*v[2535]*v[2533]*v[2531] - v[2535]*v[2429] - v[2533]*v[2466] - v[2468]*v[2531] + v[1816])-60*(6*v[2514]*v[2535]*v[2531] - 3*v[2514]*v[2466] - v[2513]*v[2531] - 6*pow(v[2535], 3)*v[2531] + 6*pow(v[2535], 2)*v[2466] - 3*v[2535]*v[2256] + v[2236])-90*(-v[2534]*v[2526] + v[2442])+120*(2*v[2535]*v[2534]*v[2530] - v[2535]*v[2446] - v[2534]*v[2465] - v[2469]*v[2530] + v[1833])+45*(-v[2534]*v[2501] + 2*v[2534]*pow(v[2533], 2) + v[2061] - 2*v[2533]*v[2449])-90*(2*v[2514]*v[2534]*v[2533] - v[2514]*v[2449] - 6*pow(v[2535], 2)*v[2534]*v[2533] + 2*pow(v[2535], 2)*v[2449] + 4*v[2535]*v[2534]*v[2468] + 4*v[2535]*v[2469]*v[2533] - 2*v[2535]*v[1836] - v[2534]*v[2258] - v[2259]*v[2533] - 2*v[2469]*v[2468] + v[1401])+15*(6*pow(v[2514], 2)*v[2534] - 36*v[2514]*pow(v[2535], 2)*v[2534] + 24*v[2514]*v[2535]*v[2469] - 6*v[2514]*v[2259] + 8*v[2513]*v[2535]*v[2534] - 4*v[2513]*v[2469] - v[2512]*v[2534] + 24*pow(v[2535], 4)*v[2534] - 24*pow(v[2535], 3)*v[2469] + 12*pow(v[2535], 2)*v[2259] - 4*v[2535]*v[2239] + v[2219])-120*(v[2515])+144*(-v[2535]*v[2521] + v[2456])+90*(-v[2533]*v[2526] + v[2424])-90*(-v[2514]*v[2526] + 2*pow(v[2535], 2)*v[2526] - 2*v[2535]*v[2461] + v[2251])+40*(v[2490] - pow(v[2530], 2))-120*(2*v[2535]*v[2533]*v[2530] - v[2535]*v[2428] - v[2533]*v[2465] - v[2468]*v[2530] + v[1815])+40*(6*v[2514]*v[2535]*v[2530] - 3*v[2514]*v[2465] - v[2513]*v[2530] - 6*pow(v[2535], 3)*v[2530] + 6*pow(v[2535], 2)*v[2465] - 3*v[2535]*v[2255] + v[2235])-15*(-3*v[2501]*v[2533] + v[2500] + 2*pow(v[2533], 3))+45*(-v[2514]*v[2501] + 2*v[2514]*pow(v[2533], 2) + 2*pow(v[2535], 2)*v[2501] - 6*pow(v[2535], 2)*pow(v[2533], 2) - 2*v[2535]*v[2127] + 8*v[2535]*v[2533]*v[2468] + v[1931] - 2*v[2533]*v[2258] - 2*pow(v[2468], 2))-15*(6*pow(v[2514], 2)*v[2533] - 36*v[2514]*pow(v[2535], 2)*v[2533] + 24*v[2514]*v[2535]*v[2468] - 6*v[2514]*v[2258] + 8*v[2513]*v[2535]*v[2533] - 4*v[2513]*v[2468] - v[2512]*v[2533] + 24*pow(v[2535], 4)*v[2533] - 24*pow(v[2535], 3)*v[2468] + 12*pow(v[2535], 2)*v[2258] - 4*v[2535]*v[2238] + v[2218])+1*(30*pow(v[2514], 3) - 270*pow(v[2514], 2)*pow(v[2535], 2) + 120*v[2514]*v[2513]*v[2535] - 15*v[2514]*v[2512] + 360*v[2514]*pow(v[2535], 4) - 10*pow(v[2513], 2) - 120*v[2513]*pow(v[2535], 3) + 30*v[2512]*pow(v[2535], 2) - 6*v[2511]*v[2535] + v[2510] - 120*pow(v[2535], 6))'))