clc;
clear;

% Change these points to change shape of curve. Curve starts and ends at P0
% and P3 respectively.
P0 = [0 0 0]';
P1 = [0 2 2]';
P2 = [1 1 2]';
P3 = [1 1 0]';

t = linspace(0, 1, 20);
B = zeros(3, 20);
idx = 1;

for step = t
    B(:, idx) = (1-step)^3*P0 + 3*(1-step)^2*step*P1 + 3*(1-step)*step^2*P2 + step^3*P3;
    idx = idx+1;
end

plot3(B(1,:), B(2,:), B(3, :))