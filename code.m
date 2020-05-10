%let us clean something
clear all;
close all;
clc;



%% Information and help
subanswer=inputdlg({'The Participant Number','Gender[1:Male,2:Female,3:]','Age','Race','Initials'},'Information',1);
helpdlg('The experiment will start in 3 seconds.','Help')
WaitSecs(3);



%% Screen
Screen('Preference','SkipSyncTests',1);
rng('shuffle');
[window,rect]=Screen('OpenWindow',0,[],[]);
Screen('BlendFunction',window, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

win_width=rect(3);
win_height=rect(4);
window_w=win_width;
window_h=win_height;
x_center=win_width/2;
y_center=win_height/2;%屏幕中心点



%% 指导语是不是也应该在这里实现



%% Blocks定义Block
nBlock=4;
nblock=nBlock/2;
block_oneface=zeros(1,9);



%% Loading
cd('C:\Users\ty\Desktop\code11\Social_Assessment\Social_Assessment\Black');
for i=1:40%for循环
    black_img=imread(['B-',num2str(i),'.jpg']);
    pointer_face(i)=Screen('MakeTexture', window ,uint8(black_img));
    Screen('DrawText',window,'Loading...',x_center,y_center-75);
    Screen('DrawText',window,sprintf('%d%%',i),x_center,y_center+25);
    Screen('Flip',window);
end
cd ..



%% Image%demo尺寸
img_width=size(black_img,2)/5;
img_height=size(black_img,1)/5;



%% Displaying
for b=1:1
Screen('DrawTexture', window, pointer_instruction(b), [], []);
Displaying_Time = 1;%所以这个是什么意思
Waiting_Time = 1;
Screen('Flip',window);
end
WaitSecs(8);
ab=Ask(window,'Are you ready? You can type "1" to start when you are ready.',[],[],'GetChar');
disp(upper(ab));

result=cell(nblock*2,16); %%%
itrial=0; %%%



%% Result

num1=subanswer(1);
num1=cell2mat(num1);
filename_result=['result',num1,num2str(num1),'.mat'];
cd('C:\Users\ty\Desktop\code\Result');
saveresult='result';
save(filename_result,saveresult);
cd ..
