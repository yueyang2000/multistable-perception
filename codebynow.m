ioption.Resize='on';    
subanswer=inputdlg({'编号','性别','年龄'},'被试信息',1,{'','',''},ioption);%信息输入对话框
cd('E:\mpsrt');%这是存图片的文件夹
Screen('Preference', 'SkipSyncTests', 2);
[window,rect]=Screen('OpenWindow',0,[],[]);

win_width=rect(3);
win_height=rect(4);
window_w=win_width;
window_h=win_height;
x_center=win_width/2;
y_center=win_height/2;%屏幕中心点
nblock=6;
ntrial=9;
result1=zeros(nblock,ntrial,100);
result2=zeros(nblock,ntrial,100);

count=zeros(nblock,ntrial);%result1,2和count存实验结果。
%result1存每次逆转到模式1的时间，results2存每次逆转到模式2的时间
%count存逆转次数（count-1是逆转次数）

%实验开始前的提示语
note=imread(['note','.png']);
Screen('PutImage',window,note);
Screen('Flip',window);
while(~KbCheck) 
end;

%开始第一个block的第一次trial
thisblock=1;
thistrial=1;
count1=0;
count2=0;

%展示指导语
guidance=imread(['guidance','.png']);
Screen('PutImage',window,guidance);
Screen('Flip',window);
WaitSecs(3);

%展示任务信号
task=imread(['task','.png']);
Screen('PutImage',window,task);
Screen('Flip',window);
WaitSecs(1);

%展示注视点
fixation=imread(['fixation','.png']);
Screen('PutImage',window,fixation);
Screen('Flip',window);
WaitSecs(1);


%展示刺激（时间可调）
cd('E:\mpsrt\rsjpg');
for i=1:118
    tryy=imread(['rsframe',num2str(i),'.jpg']);
    rs(i)=Screen('MakeTexture',window,uint8(tryy));
end
FlushEvents('keydown');
start=GetSecs;
for i=1:300   %和WaitSecs一起控制时间
    imod=mod(i,118);%mod取余
    imod=imod+1;
    Screen('DrawTexture',window,rs(imod),[],[]); 
    Screen('Flip',window);
    WaitSecs(0.1);  %控制转动快慢，和for循环i的上界一起控制时间

    [keyisdown,secs,keycode]=KbCheck;%下边检测键盘输入时间和逆转次数。逻辑有一点点复杂，如果有必要可以例会上说一下。
    if(keycode(68)==1&&lasttime1==0)  
    count(thisblock,thistrial)=count(thisblock,thistrial)+1;
    count1=count1+1;
    lasttime1=1;
    result1(thisblock,thistrial,count1)=secs-start;
    end
    if(keycode(68)==0) lasttime1=0; end

    if(keycode(74)==1&&lasttime2==0)  
    count(thisblock,thistrial)=count(thisblock,thistrial)+1;
    lasttime2=1;
    count2=count2+1;
    result2(thisblock,thistrial,count2)=secs-start;
    end
    if(keycode(74)==0) lasttime2=0; end
    
    FlushEvents('keydown');
end

WaitSecs(1);

%other trials  %用同样的流程实现这个block中的其他trial
%othet blocks  %用同样的流程实现其他block
sca;


%finish and save
save subanswer subanswer;
save result1 result1;
save result2 result2;
save count count;
%存变量到运行文件夹
