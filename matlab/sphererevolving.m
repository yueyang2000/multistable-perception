clear all;close all;clc;
figure( 'name' , ' s_r' ); 
whitebg('black');%����������������ɫ
axis equal;
axis([-1,1,-1,1]);
hold on ;
N=200;%���õ�ĸ���N
K=2;%���ú�������ı���K:1
omg=pi/3;%Ӱ���ת�����ٶȣ�ԽС�ٶ�Խ����
dt=0.05; %Ӱ���ٶȺ;�ϸ��ԽС���ٶ�Խ����
b=2*pi/omg/dt;%����֡���ĳ���,����ǡ����һ������;һ�㲻�øģ�
R=1;
y=rand(1,N)*2-1;
r0=(R^2-y.^2).^(1/2);
phi=2*pi*rand(1,N)-pi;
x=r0.*cos(phi);
for m=1:N
    if m<N*K/(K+1)
        p(m)=plot(x(m),y(m), 'color' , 'w' , 'marker' , '.' , 'markersize' ,15); %�м��r�Ǻ�ɫ�������size�ı��Ĵ�С
    else
        p(m)=plot(x(m),y(m), 'color' , 'w' , 'marker' , '.' , 'markersize' ,15); %�м��g����ɫ�������size�ı��Ĵ�С
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