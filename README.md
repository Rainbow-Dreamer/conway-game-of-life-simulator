# conway-game-of-life-simulator

[中文](#conway-game-of-life-simulator中文版介绍) English

This is a simple conway's game of life editor and simulator, you can draw any lifes easily in this software and watch their evolutions, and you can customize the BS rules and the images of lives and background, and so on.

Use mouse's left button to draw lives, use mouse's right button to erase lives.

On keyboard:  
press C to clear all of the lives currently on the screen  
press space to start evolutions of the lives currently on the screen  
press Q to pause current evolutions

You can change settings in the file `康威生命游戏配置参数.py`

* B: Born parameter in BS rule of conway's game of life
* S: Survive parameter in BS rule of conway's game of life
* title_name: the title of the screen
* screen_size: the size of the screen, width, height in pixels
* block_size: the size of blocks in pixels
* background_img: the image path of background image
* life_img: the image path of life image
* read_file: the image path of text file if you want to read a whole lives' pattern into this simulator, otherwise leave it as `None`

Note: If you want to read a whole lives' pattern into this simulator, you can set `read_file` in the settings file to image path of a text file, the text file must be in the form that uses `o` to represent lives and ` ` to represent no lives. (just whitespaces for no lives)

The default background image is a whole black image, you can change the background images in the settings file.  
You can also change the images of lives in the settings file.  
If you want to change the BS rule of conway's game of life, you can change B and S in the settings file, please note that B must be an integer and S must be a list of integers. After that, save the settings file and then restart the simulator to have the changed settings take effect.

Here is a picture of this onway's game of life editor and simulator:
![image](previews/1.jpg)

# conway-game-of-life-simulator中文版介绍

中文 [English](#conway-game-of-life-simulator)

这是一个简单的康威生命游戏的模拟器，你可以在这个软件里简单地描绘生命并且看他们演化，你可以设置BS规则，改变生命和背景的图片等等。

用鼠标的左键画出生命，用鼠标的右键抹去生命。

在键盘上:
按C键清除当前屏幕上所有的生命。
按空格键启动当前在屏幕上的生命的进化
按Q键暂停当前的演化

你可以在文件康威生命游戏配置参数.py中改变设置:

B：康威生命游戏的BS规则中的出生参数
S：康威生命游戏的BS规则中的生存参数
title_name：屏幕的标题
screen_size：屏幕的大小，宽度和高度，单位为像素
block_size: 块的大小，单位是像素
background_img: 背景图片的图片路径
life_img: 生活图片的图片路径
read_file: 文本文件的路径，如果你想读取整个生命的图案到这个模拟器中，否则留作`None`

注意：如果你想把整个生命的图案读入这个模拟器，你可以在设置文件中把read_file设置为一个文本文件的图像路径，这个文本文件必须是用o来代表生命和代表无生命的形式。(只是用空格表示没有生命)

默认的背景图像是整个黑色的图像，你可以在设置文件中改变背景图像。
你也可以在设置文件中改变生命的图像。
如果你想改变康威生命游戏的BS规则，你可以在设置文件中改变B和S，请注意，B必须是一个整数，S必须是一个整数的列表。之后，保存设置文件，然后重新启动模拟器，使改变的设置生效。

下面是这个康威生命游戏编辑器和模拟器的界面图:
![image](previews/1.jpg)
