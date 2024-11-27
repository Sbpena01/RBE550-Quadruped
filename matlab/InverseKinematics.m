clc;
clear;

% Define symbolic variables
syms theta1 theta2 theta3 real;
syms d1 d2 d3 real;  % Offset translations
a1 = 0; a2 = 0; a3 = 0;  % Link lengths (0 based on your DH parameters)
alpha1 = 0; alpha2 = pi/2; alpha3 = pi/2;  % Twist angles

% DH Parameters
% For joint 1 (rear_left_shoulder)
T1 = [cos(theta1), -sin(theta1)*cos(alpha1),  sin(theta1)*sin(alpha1), a1*cos(theta1);
      sin(theta1),  cos(theta1)*cos(alpha1), -cos(theta1)*sin(alpha1), a1*sin(theta1);
      0,            sin(alpha1),              cos(alpha1),             d1;
      0,            0,                         0,                        1];
  
% For joint 2 (rear_left_leg)
T2 = [cos(theta2), -sin(theta2)*cos(alpha2),  sin(theta2)*sin(alpha2), a2*cos(theta2);
      sin(theta2),  cos(theta2)*cos(alpha2), -cos(theta2)*sin(alpha2), a2*sin(theta2);
      0,            sin(alpha2),              cos(alpha2),             d2;
      0,            0,                         0,                        1];

% For joint 3 (rear_left_foot)
T3 = [cos(theta3), -sin(theta3)*cos(alpha3),  sin(theta3)*sin(alpha3), a3*cos(theta3);
      sin(theta3),  cos(theta3)*cos(alpha3), -cos(theta3)*sin(alpha3), a3*sin(theta3);
      0,            sin(alpha3),              cos(alpha3),             d3;
      0,            0,                         0,                        1];

% Forward Kinematics: Multiply transformation matrices
T_01 = T1;  % Transformation from base to joint 1
T_12 = T1 * T2;  % Transformation from joint 1 to joint 2
T_23 = T1 * T2 * T3;  % Transformation from joint 2 to joint 3

% Display the final transformation matrix from the base to the end effector
disp('The transformation matrix from the base to the end effector is:');
T_final = T_01 * T_12 * T_23;
disp(T_final);

% Extract the position (x, y, z) of the end effector
end_effector_pos = T_final(1:3, 4);  % Extracting the position vector
disp('The position of the end effector is:');
disp(end_effector_pos);