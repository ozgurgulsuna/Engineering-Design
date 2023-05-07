%% Find Equadistance Point on Ground Between Two Poles %%




min = 13;
main = 42;

min_height = 35;
top_pole_sep = 20;
alpha = rad2deg(atan(min_height/(min_height-top_pole_sep/2)));
gamma = rad2deg(atan(min_height/(min_height+top_pole_sep/2)));

main*cos(deg2rad(alpha))
main*sin(deg2rad(alpha))

syms L d theta mu 
left_pole = min*sin(deg2rad(alpha)) % 13 cm is the min distance, answer is the height
right_pole = (main-7)*sin(deg2rad(gamma)) % main pole lenght 46 - 7 the maximum distance, answer is the height
between = min*cos(deg2rad(alpha))+(main-7)*cos(deg2rad(gamma)) 
% left_pole = 9.985;
% right_pole = 21;
% between = 34.6564 ; 



eq1 = L*cos(theta) + L*cos(mu) == between;
eq2 = L*sin(theta) == right_pole;
eq3 = L*sin(mu) == left_pole;
eq4 = d == L*cos(mu)-min*cos(deg2rad(alpha));
eq5 = 2*L*L == left_pole^2+right_pole^2+(L*cos(mu))^2+(L*cos(theta))^2;

S = vpasolve([eq1 eq2 eq3 eq4],[L d theta mu]);

S.L
S.d
