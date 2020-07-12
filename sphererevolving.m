clear all;close all;clc;
figure( 'name' , ' s_r' ); 
whitebg('black');%更改坐标区背景颜色
axis equal;
axis([-1,1,-1,1]);
hold on ;
N=200;%设置点的个数N
K=2;%设置红绿两点的比例K:1
omg=pi/3;%影响点转动的速度，越小速度越慢；
dt=0.05; %影响速度和精细度越小，速度越慢；
b=2*pi/omg/dt;%动画帧数的长度,这里恰好是一个周期;一般不用改；
R=1;
y=rand(1,N)*2-1;
r0=(R^2-y.^2).^(1/2);
phi=2*pi*rand(1,N)-pi;
x=r0.*cos(phi);
for m=1:N
    if m<N*K/(K+1)
        p(m)=plot(x(m),y(m), 'color' , 'w' , 'marker' , '.' , 'markersize' ,15); %中间的r是红色，后面的size改变点的大小
    else
        p(m)=plot(x(m),y(m), 'color' , 'w' , 'marker' , '.' , 'markersize' ,15); %中间的g是绿色，后面的size改变点的大小
    end
end


ax = gca;
ax.YAxis.Visible = 'off'; 
ax.XAxis.Visible = 'off'; 
ax.Units = 'pixels';
pos = ax.Position;
frame = getframe(ax);
im=frame2im(frame);
k = 1;
[I{k},map{k}]=rgb2ind(im,256);
imwrite(I{k},map{k,1},'revolving_sphere.gif','gif','Loopcount',Inf,'DelayTime',0.2);
k = k + 1;
i=1;
while i < (b-1)
    for m=1:N
        x(m)=r0(m)*cos(omg*i*dt+phi(m)); 
        y(m)=y(m);
        set(p(m), 'xdata' ,x(m), 'ydata' ,y(m));
    end
    ax = gca;
    ax.Units = 'pixels';
    pos = ax.Position;
    frame = getframe(ax);
    im=frame2im(frame);
    [I{k},map{k}]=rgb2ind(im,256);
    imwrite(I{k},map{k},'revolving_sphere.gif','gif','WriteMode','append','DelayTime',0.1); 
    k = k + 1; 
    i = i + 1;
end