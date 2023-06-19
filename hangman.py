import random
from tkinter import *
from tkinter import messagebox

#declaring score and run variables
score = 0
run = True

# main loop, i.e. opening of main window of game
while run:
    window = Tk()
    window.geometry('905x700')
    window.title('HANGMAN')
    window.config(bg = '#FFFFFF')

    #initialising count variables
    lose_count = 0
    win_count = 0

    # choosing word
    file = open('fruits.txt','r')
    l = file.readlines()
    index = random.randint(0,len(l))
    selected_word = l[index].strip('\n')
    
    # creation of word dashes variables
    x = 250
    for i in range(0,len(selected_word)):
        exec('d{}=Label(window,text="_",bg="#FFFFFF",font=("arial",40))'.format(i))
        exec('d{}.place(x={},y={})'.format(i,x,430))
        x += 60
        
    #letters icon
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letter in alphabet:
        exec('{}=PhotoImage(file="{}.png")'.format(letter,letter))
        
    # hangman images
    hmi = ['h1','h2','h3','h4','h5','h6','h7']
    for hangman in hmi:
        exec('{}=PhotoImage(file="{}.png")'.format(hangman,hangman))
        
   #letters placement
    button = [['b1','a',0,500],['b2','b',70,500],['b3','c',140,500],['b4','d',210,500],['b5','e',280,500],['b6','f',350,500],['b7','g',420,500],['b8','h',490,500],['b9','i',560,500],['b10','j',630,500],['b11','k',700,500],['b12','l',770,500],['b13','m',840,500],['b14','n',0,570],['b15','o',70,570],['b16','p',140,570],['b17','q',210,570],['b18','r',280,570],['b19','s',350,570],['b20','t',420,570],['b21','u',490,570],['b22','v',560,570],['b23','w',630,570],['b24','x',700,570],['b25','y',770,570],['b26','z',840,570]]
    for q1 in button:
        exec('{}=Button(window,bd=0,command=lambda:check("{}","{}"),bg="#FFFFFF",activebackground="#E7FFFF",font=10,image={})'.format(q1[0],q1[1],q1[0],q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0],q1[2],q1[3]))
        
    #hangman placement
    han = [['c1','h1'],['c2','h2'],['c3','h3'],['c4','h4'],['c5','h5'],['c6','h6'],['c7','h7']]
    for p1 in han:
        exec('{}=Label(window,bg="#FFFFFF",image={})'.format(p1[0],p1[1]))

    # placement of first hangman image
    c1.place(x = 300,y =0)
    
    
    # exit buton
    def close():
        global run
        answer = messagebox.askyesno('ALERT','YOU WANT TO EXIT THE GAME?')
        if answer:
            run = False
            window.destroy()
            
    e1 = PhotoImage(file = 'button_exit.png')
    ex = Button(window,bd = 0,command = close,bg="#FFFFFF",activebackground = "#E7FFFF",font = 10,image = e1)
    ex.place(x=770,y=10)
    s2 = 'SCORE:'+str(score)
    s1 = Label(window,text = s2,bg = "#FFFFFF",font = ("arial",25))
    s1.place(x = 10,y = 10)

        #sounds for game
    def correct_answer_sound():
        playsound("correct_answer_tring!.mp3")
        
    def wrong_answer_sound():
        playsound("wrong_answer_dejected.mp3")

    def game_win__sound():
        playsound("game_success_tring!.mp3")

    def lost_game_sound():
        playsound("game_fail_toptolow.mp3")

        
    # button press check function
    def check(letter,button):
        global lose_count,win_count,run,score
        exec('{}.destroy()'.format(button))
        if letter in selected_word:
            for i in range(0,len(selected_word)):
                if selected_word[i] == letter:
                    win_count += 1
                    exec('d{}.config(text="{}")'.format(i,letter.upper()))
                    
            if win_count == len(selected_word):
                score += 1
                answer = messagebox.askyesno('GAME OVER','YOU WON!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    window.destroy()   
                else:
                    run = False
                    window.destroy()
        else:
            lose_count += 1
            exec('c{}.destroy()'.format(lose_count))
            exec('c{}.place(x={},y={})'.format(lose_count+1,300,0))
            if lose_count == 6:
                answer = messagebox.askyesno('GAME OVER','YOU LOST!\nCORRECT WORD IS: {}\nWANT TO PLAY AGAIN?'.format((selected_word.upper())))
                if answer:
                    run = True
                    score = 0
                    window.destroy()
                else:
                    run = False
                    window.destroy()         
    window.mainloop()

