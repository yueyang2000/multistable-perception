
imgs(1).('img')=imread([prefix num2str(1) '.' postfix]);

wrect=Screen('Rect',wptr);%获取窗口大小
Screen('PutImage',wptr,imgs(1).img);%向窗口中写入图像
trect=Screen('TextBounds',wptr,'按空格键继续');
x=wrect(3)-rect2(3)-10; y=wrect(4)-trect2(4)-10; %设置绘制文本坐标
Screen('DrawText',wptr,'按空格键继续',x,y);

Screen('Flip',wptr);%页面切换
spaceKey=KbName('space');%获取按键的扫描码
ListenChar(2);%屏幕掉Matlab命令窗口对案件信息的接收
while true
    [~,~,keyCode]=KbCheck;
    if keyCode(spaceKey)
        break;
    elseif keyCode
        