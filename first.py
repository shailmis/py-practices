colors = ["red","green","black","white","blue"]
names = ["shailesh","Kamalini","hanu","shubh","Urmila","Shalini"]
for color in colors:
    print(color)
for color in reversed(colors):
    print(color)
for i , color in enumerate(colors):
    print(f'{color} in position {i}')
for color,name in zip(colors,names):
    print(f'{color} --> {name}')
    
    