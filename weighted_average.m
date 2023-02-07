## weighted average 
## determine the nearest 5 points (construct the weighted point location) 

%% fine the five smallest pairwise euclidean distance with their coordinates in column2,3
[D,I] = pdist2(X,Y,'euclidean','Smallest',5); 

%% extract out the coordinate 

correlation = corrcoef (x, y); 
cor_x =correlation(:,1); 
cor_x =correlation(2,:)-[0 1];
cor_y =correlation(:,2); 
cor_y =cor_y(1,:);
det_x =x-cor_x;
det_x =det_x(:,1);
det_y =y-cor_y; 

                
D = pdist2(X,Y,Distance);  %% calcualte all the distance between different points 
pt=[dist x y z];            %% declear pt into matrix (distance,x,y,z columns)
pt=sort (pt,'ascend');      %% sort the calcualted distance ascendingly 
dist=sort (dist,'ascend');  %% sort the distacne indiviually ascendingly 
sp=pt(1:5, :);              %% extract out the nearest 5 points and distance

## extract the nearest five coodinate
dist=sp(:,1);        %%get the nearest five distance in matrix column 1
spx= sp(:,2);        %%get the nearest five x in matrix column 2
spy= sp(:,3);        %%get the nearest five y in matrix column 3
spz= sp(:,4);        %%get the nearest five z in matrix column 4

## construct the weighted point location
[C_x,C_Y] = kmeans(x,1);
[C_y,C_X] = kmeans(y,1); 
## the center "weighted" point 
cwpt =[C_X C_Y];
 
plot3 = overall;

## determine the centered point 
cpx= mean(spx);      %%get the mean of centered point x 
cpy= mean(spy);      %%get the mean of centered point y
cpz= mean(spz);      %%get the mean of centered point z
cp=[cpx cpy cpz];    %%get the centered point 

## calculate the weighting 
w= 1/dist.^2; 
z_weighted= (cpz*w)/w;

## calculate the new populated of all point 
w_x =x-cpx; %%get the points minus weighted point x
w_y =y-cpy; %%get the points minus weighted point x
w_z =z*z_weighted; %%get the points minus weighted point z
w_xyz= [w_x w_y w_z]; 

% for loop to draw the 50x50 interpolation graph 
for  i1 = 1 : size(grid_x,1) 
 for i2 = 1 : size(grid_y,1) 
     Q  =[1  grid_x(i1) grid_y(i2) grid_x(i1).*grid_y(i2)]; 
     q  =pinv(Q)*zwz; 
     grid_z(i1, i2) = A*a; 
 end 
end 

## interpolation with interval 2m
grid_wz = zeros(size(grid_x,1), size(grid_x,1));

% for loop to draw the 50x50 interpolation graph 
for  i1 = 1 : size(grid_x,1) 
 for i2 = 1 : size(grid_y,1)  
     w_a= w_xyz (:,3);
  grid_wz (i1, i2), w_a;
 end 
end 
