# conway-game-of-life-simulator
 
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

Note: If you want to read a whole lives' pattern into this simulator, you can set `read_file` in the settings file to image path of a text file,  
the text file must be in the form that uses `o` to represent lives and ` ` to represent no lives. (just whitespaces for no lives)

这是一个简单的康威生命游戏的模拟器，你可以在这个软件里简单地描绘生命并且看他们演化，你可以设置BS规则，改变生命和背景的图片等等。
