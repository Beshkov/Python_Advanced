file = open("text.txt", "w")
file.write('I just created my first file!\n')
file.close()

file = open('text.txt', 'a')
zug = ['Orks are green', 'the grass is green', 'Are Orks grass?']
file.writelines([zugzug + '\n' for zugzug in zug])
file.close()