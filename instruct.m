
imgs(1).('img')=imread([prefix num2str(1) '.' postfix]);

wrect=Screen('Rect',wptr);%��ȡ���ڴ�С
Screen('PutImage',wptr,imgs(1).img);%�򴰿���д��ͼ��
trect=Screen('TextBounds',wptr,'���ո������');
x=wrect(3)-rect2(3)-10; y=wrect(4)-trect2(4)-10; %���û����ı�����
Screen('DrawText',wptr,'���ո������',x,y);

Screen('Flip',wptr);%ҳ���л�
spaceKey=KbName('space');%��ȡ������ɨ����
ListenChar(2);%��Ļ��Matlab����ڶ԰�����Ϣ�Ľ���
while true
    [~,~,keyCode]=KbCheck;
    if keyCode(spaceKey)
        break;
    elseif keyCode
        