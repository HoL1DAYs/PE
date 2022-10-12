import sys
import tkinter as tk
from tkinter import ttk
from tkvideo import tkvideo

import os
import gobject
import gst


def on_sync_message(bus, message, window_id):
    if not message.structure is None:
        if message.structure.get_name() == 'prepare-xwindow-id':
            image_sink = message.src
            image_sink.set_property('force-aspect-ratio', True)
            image_sink.set_xwindow_id(window_id)


gobject.threads_init()

window = tk.Tk()
window.title('PE')
window.geometry("1600x800+50+20")
frame_ex = tk.Frame(window, bg='green')
frame_main = tk.Frame(window, bg='blue')
frame_home = tk.Frame(window, bg='red')
frame_name = tk.Frame(window, bg='white')
frame_video = tk.Label(window, bg='#000000')
frame_home.place(relx=0, rely=0, relheight=1/4, relwidth=1/3)
frame_ex.place(relx=0, rely=1/4, relheight=3/4, relwidth=1/3)
frame_main.place(relx=1/3, rely=34/48, relheight=14/48, relwidth=2/3)
frame_name.place(relx=1/3, rely=0, relheight=1/16, relwidth=2/3)
frame_video.place(relx=1/3, rely=1/21, relheight=2/3, relwidth=2/3)


def sila():
    for widget in frame_ex.winfo_children():
        widget.destroy()
    def sila_1():
        for widget in frame_main.winfo_children():
            widget.destroy()
        for widget in frame_name.winfo_children():
            widget.destroy()

        window_id = frame_video.winfo_id()
        player = gst.element_factory_make('playbin2', 'player')
        player.set_property('video-sink', None)
        player.set_property('uri', "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\file_1.mp4" % (os.path.abspath(sys.argv[1])))
        player.set_state(gst.STATE_PLAYING)
        bus = player.get_bus()
        bus.add_signal_watch()
        bus.enable_sync_message_emission()
        bus.connect('sync-message::element', on_sync_message, window_id)


        video = tkvideo("C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\file_1.mp4", frame_video, loop=1, size=(1068, 534))
        video.play()

        ex_name = tk.Label(frame_name, text='Упражнение №1 сгибание и разгибание рук в упоре лежа')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Упор лежа, ноги вместе, туловище прямое, согнуть руки до касания грудью пола, разгибая руки принять положение упор лежа. Упражнение выполняется без остановки. Для контроля разрешается использовать специальное техническое приспособление'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Прогиб в спине.
2. Не касание грудью пола.
3. Не фиксация положения упора лежа.
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 38
        4 – 36
        3 – 30
2 курс: 5 – 45
        4 – 40
        3 – 36
3 курс и старше: 
        5 – 50
        4 – 43
        3 – 38
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)



    def sila_2():
        for widget in frame_main.winfo_children():
            widget.destroy()
        for widget in frame_name.winfo_children():
            widget.destroy()

        video = tkvideo("C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\file_2.mp4", frame_video, loop=1,
                            size=(1068, 534))
        video.play()
        ex_name = tk.Label(frame_name, text='Упражнение N 2 наклоны туловища вперед')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Положение лежа на спине, руки за голову, пальцы в «замок», ноги закреплены, наклонить туловище вперед до касания локтями коленей, возвратиться в исходное положение до касания пола лопатками. Упражнение выполняется в течение одной минуты. Разрешается незначительное сгибание ног.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Не касание локтями колена.
2. Не касание лопатками пола (мата).
                '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 48
        4 – 45
        3 – 40
2 курс: 5 – 55
        4 – 50
        3 – 45
3 курс и старше: 
        5 – 58
        4 – 53
        3 – 48
        '''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)


    def sila_3():
        for widget in frame_main.winfo_children():
            widget.destroy()

        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo("C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\file_3.mp4", frame_video, loop=1,
                        size=(1068, 534))
        video.play()

        ex_name = tk.Label(frame_name, text='Упражнение N 4 подтягивание на перекладине')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Вис хватом сверху (ноги вместе), сгибая руки, подтянуться (подбородок выше грифа перекладины), разгибая руки, опуститься в вис. Положение виса фиксируется. Разрешается незначительное сгибание и разведение ног, незначительное отклонение тела от неподвижного положения в висе.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Маховые движения ногами.
2. Рывок руками.
3. Отсутствие фиксации.
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 12
        4 – 10
        3 – 8
2 курс: 5 – 15
        4 – 13
        3 – 10
3 курс и старше: 
        5 – 18
        4 – 14
        3 – 12
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)


    def sila_4():
        for widget in frame_main.winfo_children():
            widget.destroy()

        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo("C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\file_4.mp4", frame_video, loop=1,
                        size=(1068, 534))
        video.play()

        ex_name = tk.Label(frame_name, text='Упражнение N 5 поднимание ног к перекладине')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Вис хватом сверху (ноги вместе), поднять ноги к перекладине до касания и опустить их вниз. Положения виса фиксируется. Разрешается незначительное сгибание и разведение ног. Запрещается выполнение движений махом.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Запрещается выполнение движений рывком и махом. 
2. Не касание ног перекладины.
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 14
        4 – 11
        3 – 8
2 курс: 5 – 21
        4 – 16
        3 – 11
3 курс и старше: 
        5 – 24
        4 – 19
        3 – 14
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_5():
        for widget in frame_main.winfo_children():
            widget.destroy()
        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo("C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\file_5.mp4", frame_video, loop=1,
                        size=(1068, 534))
        video.play()

        ex_name = tk.Label(frame_name, text='Упражнение N 6 подъем переворотом на перекладине')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Вис хватом сверху (ноги вместе), сгибая руки, поднять ноги к перекладине и переворачиваясь вокруг оси снаряда выйти в упор на прямые руки. Положения виса и упора фиксируются, опускание в вис выполняется произвольным способом. Разрешается незначительное сгибание и разведение ног, незначительное отклонение тела от неподвижного положения в висе. Запрещается выполнение движений махом.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Отсутвие фиксации внизу и вверху. 
2. Движение махом. 
3. Касание подбородка перекладины.
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 7
        4 – 6
        3 – 5
2 курс: 5 – 10
        4 – 8
        3 – 6
3 курс и старше: 
        5 – 12
        4 – 9
        3 – 7
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_6():
        for widget in frame_main.winfo_children():
            widget.destroy()
        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo("C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\file_7.mp4", frame_video, loop=1,
                        size=(1068, 534))
        video.play()

        ex_name = tk.Label(frame_name, text='Упражнение N 7 подъем силой на перекладине')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Вис хватом сверху (ноги вместе), сгибая руки, поставить в упор сначала одну согнутую руку, затем - другую; продолжая движение, выйти в упор на прямые руки. Положение виса и упора фиксируются; опускание в вис выполняется произвольным способом. Разрешается подъем силой на обе руки, незначительное сгибание и разведение ног, незначительное отклонение тела от неподвижного положения в висе. Запрещается выполнение движений рывком и махом.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Отсутствие фиксации. 
2. Выполнение махом.
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 5
        4 – 4
        3 – 3
2 курс: 5 – 7
        4 – 6
        3 – 4
3 курс и старше: 
        5 – 8
        4 – 6
        3 – 5
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_7():
        for widget in frame_main.winfo_children():
            widget.destroy()
        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo("C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\file_9.mp4", frame_video, loop=1,
                        size=(1068, 534))
        video.play()

        ex_name = tk.Label(frame_name, text='Упражнение N 9 сгибание и разгибание рук в упоре на брусьях')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Упор на прямых руках, сгибая руки, опуститься в упор на согнутых руках; разгибая руки, выйти в упор. Положение упора фиксируется; при опускании руки сгибаются полностью. Разрешается незначительное сгибание и разведение ног. Запрещается выполнение движений махом.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Отжимание выполнено со сгибом менее (более) 90 градусов.
2. Отсутствие фиксации внизу и вверху. 
3. Поднятые к верху плечи. 
4. Локти, не прижатые к туловищу.
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 25
        4 – 23
        3 – 18
2 курс: 5 – 33
        4 – 28
        3 – 23
3 курс и старше: 
        5 – 35
        4 – 30
        3 – 25
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_8():
        for widget in frame_main.winfo_children():
            widget.destroy()
        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo("C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\file_10.mp4", frame_video, loop=1,
                        size=(1068, 534))
        video.play()

        ex_name = tk.Label(frame_name, text='Упражнение N 10 угол в упоре на брусьях')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Упор на прямых руках, поднять прямые ноги и удерживать их горизонтально над жердями. Время выполнения упражнения определяется с момента фиксации положения «угол» до момента опускания пяток ног ниже жердей.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Сгибание ног в коленях. 
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 17,0
        4 – 14,5
        3 – 9,5
2 курс: 5 – 24,5
        4 – 19,5
        3 – 14,5
3 курс и старше: 
        5 – 29,0
        4 – 22,0
        3 – 17,0
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_9():
        for widget in frame_main.winfo_children():
            widget.destroy()
        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo("C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\file_11.mp4", frame_video, loop=1,
                        size=(1068, 534))
        video.play()

        ex_name = tk.Label(frame_name, text='Упражнение N 11 рывок гири, вес 24 кг')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Стойка - ноги врозь, хватом сверху одной рукой за дужку гири, последовательно поднимать гирю вверх и опускать вниз, не касаясь пола, сначала одной рукой, затем без отдыха после смены рук - другой. Положение гири вверху фиксируется на прямой руке, смена рук осуществляется один раз на замахе вперед. Запрещается дожимать гирю, отдыхать в положении, когда гиря опущена вниз, касаться свободной рукой частей тела.
Установлены две весовые категории: до 70 кг, 70 кг и выше
'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Запрещается отдыхать в положении, когда гиря опущена вниз, касаться свободной рукой частей тела. 
2. Отсутствие фиксации гири вверху.
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 43
        4 – 40
        3 – 36
2 курс: 5 – 50
        4 – 45
        3 – 40
3 курс и старше: 
        5 – 53
        4 – 48
        3 – 43
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_10():
        for widget in frame_main.winfo_children():
            widget.destroy()
        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo("C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\file_12.mp4", frame_video, loop=1,
                        size=(1068, 534))
        video.play()

        ex_name = tk.Label(frame_name, text='Упражнение N 12 толчок двух гирь,вес 24 кг')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Стойка - ноги врозь, хватом сверху за дужки гирь, оторвать гири от пола, поднять их на грудь, при этом гири лежат на предплечьях и плечах, руки прижаты к туловищу; вытолкнуть гири вверх и зафиксировать на прямых руках. Для повторения цикла гири на грудь. Запрещается дожимать гири и ставить их на плечи. Установлены две весовые категории: до 70 кг, 70 кг и выше.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Отсутствие фиксации гири над головой.
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 11
        4 – 10
        3 – 7
2 курс: 5 – 15
        4 – 12
        3 – 10
3 курс и старше: 
        5 – 16
        4 – 14
        3 – 11
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_11():
        for widget in frame_main.winfo_children():
            widget.destroy()
        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo("C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\file_13.mp4", frame_video, loop=1,
                        size=(1068, 534))
        video.play()

        ex_name = tk.Label(frame_name, text='Упражнение N 13 толчок двух гирь по длинному циклу,вес 24 кг')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Стойка - ноги врозь, хватом сверху за дужки гирь, оторвать гири от пола, поднять их на грудь, при этом гири лежат на предплечьях и плечах, руки прижаты к туловищу; вытолкнуть гири вверх и зафиксировать на прямых руках. Для повторения цикла гири сначала опустить на грудь, а затем – вниз, не касаясь пола. При опускании гирь на грудь отдыхать запрещается. Также запрещается отдыхать, удерживая гири, опущенные вниз. Разрешается отдыхать с гирями на груди после поднятия их из положения виса, а также с гирями, зафиксированными на прямых руках, после толчка от груди. Запрещается отдыхать, удерживая гири в положении на плечевые суставы. Установлены две весовые категории: до 70 кг, 70 кг и выше.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Отсутствие фиксации гири над головой.
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 8
        4 – 6
        3 – 4
2 курс: 5 – 11
        4 – 8
        3 – 6
3 курс и старше: 
        5 – 12
        4 – 10
        3 – 7
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    botton_sila_1 = ttk.Button(frame_ex, text='Упражнение №1 сгибание и разгибание рук в упоре лежа', command=sila_1).pack(fill='both')
    botton_sila_2 = ttk.Button(frame_ex, text='Упражнение №2 наклоны туловища вперед', command=sila_2).pack(fill='both')
    botton_sila_4 = ttk.Button(frame_ex, text='Упражнение №4 подтягивание на перекладине', command=sila_3).pack(fill='both')
    botton_sila_5 = ttk.Button(frame_ex, text='Упражнение №5 поднимание ног к перекладине', command=sila_4).pack(fill='both')
    botton_sila_6 = ttk.Button(frame_ex, text='Упражнение №6 подъем переворотом на перекладине', command=sila_5).pack(fill='both')
    botton_sila_7 = ttk.Button(frame_ex, text='Упражнение №7 подъем силой на перекладине', command=sila_6).pack(fill='both')
    botton_sila_9 = ttk.Button(frame_ex, text='Упражнение №9 сгибание и разгибание рук в упоре на брусьях', command=sila_7).pack(fill='both')
    botton_sila_10 = ttk.Button(frame_ex, text='Упражнение №10 угол в упоре на брусьях', command=sila_8).pack(fill='both')
    botton_sila_11 = ttk.Button(frame_ex, text='Упражнение №11 рывок гири, вес 24 кг', command=sila_9).pack(fill='both')
    botton_sila_12 = ttk.Button(frame_ex, text='Упражнение №12 толчок двух гирь, вес 24 кг', command=sila_10).pack(fill='both')
    botton_sila_13 = ttk.Button(frame_ex, text='Упражнение №13 толчок двух гирь по длинному циклу, вес 24 кг', command=sila_11).pack(fill='both')



def vinoslivost():
    for widget in frame_ex.winfo_children():
        widget.destroy()

    def sila_1():
        for widget in frame_main.winfo_children():
            widget.destroy()
        for widget in frame_name.winfo_children():
            widget.destroy()

        for widget in frame_video.winfo_children():
            widget.destroy()
        video = tkvideo("C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\Упражнение 43_45_46_47 бег на 400м_1км_3км_5км (НФП-2009).mp4", frame_video, loop=1,
                        size=(1068, 534))
        video.play()

        ex_name = tk.Label(frame_name, text='Упражнение N 45 бег на 1 км')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Проводятся на ровной поверхности с общего или раздельного старта. Старт и финиш оборудуются в одном месте.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Строгое огибание флажка в случае прямой. 
2. На стадионе – запрещается наступать на разграничительную линию при виражах.
3. Запрещается лидирование участника.
            '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 3,55
        4 – 4,00
        3 – 4,20
2 курс: 5 – 3,40
        4 – 3,50
        3 – 4,00
3 курс и старше: 
        5 – 3,35
        4 – 3,45
        3 – 3.55
    '''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_2():
        for widget in frame_main.winfo_children():
            widget.destroy()
        for widget in frame_name.winfo_children():
            widget.destroy()


        video = tkvideo("C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\Упражнение 43_45_46_47 бег на 400м_1км_3км_5км (НФП-2009).mp4",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()

        ex_name = tk.Label(frame_name, text='Упражнение N 46 бег на 3 км')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Проводятся на ровной поверхности с общего или раздельного старта. Старт и финиш оборудуются в одном месте.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Запрещается лидирование участника.
            '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 13,00
        4 – 13,20
        3 – 14,00
2 курс: 5 – 12,00
        4 – 12,40
        3 – 13,20
3 курс и старше: 
        5 – 11,40
        4 – 12,20
        3 – 13,00
    '''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)


    def sila_3():
        for widget in frame_main.winfo_children():
            widget.destroy()
        for widget in frame_name.winfo_children():
            widget.destroy()

        video = tkvideo(
            "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\Упражнение 43_45_46_47 бег на 400м_1км_3км_5км (НФП-2009.mp4)",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()

        ex_name = tk.Label(frame_name, text='Упражнение N 47 бег на 5 км')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Проводятся на ровной поверхности с общего или раздельного старта. Старт и финиш оборудуются в одном месте.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Запрещается лидирование участника.
            '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 21,19
        4 – 21,41
        3 – 22,50
2 курс: 5 – 20,10
        4 – 20,56
        3 – 21,41
3 курс и старше: 
        5 – 19,35
        4 – 20,34
        3 – 21,19
    '''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_4():
        for widget in frame_main.winfo_children():
            widget.destroy()
        for widget in frame_name.winfo_children():
            widget.destroy()

        video = tkvideo(
            "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\Упражнение 48,49. Марш-бросок на 5 и 10 км. (НФП-2009).mp4",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()

        ex_name = tk.Label(frame_name, text='Упражнение N 48 марш-бросок на 5 км')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Каждый военнослужащий выполняет упражнение в военной форме одежды с личным оружием (автомат с пристегнутым магазином, сумка для магазинов с одним магазином), противогаз. Запрещается всякое дополнительное крепление оружия и снаряжения, препятствующие их немедленному использованию по назначению (в том числе, дополнительные ремни, другие приспособления, не предусмотренные соответствующей формой одежды). Время определяется каждому участнику забега.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Потеря (отсутствие) головного убора и снаряжения. 
                '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 25,05
        4 – 25,30
        3 – 26,20
2 курс: 5 – 23,40
        4 – 24,35
        3 – 25,30
3 курс и старше: 
        5 – 23,15
        4 – 24,06
        3 – 25,05
        '''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_5():
        for widget in frame_main.winfo_children():
            widget.destroy()
        for widget in frame_name.winfo_children():
            widget.destroy()

        video = tkvideo(
            "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\Упражнение 48,49. Марш-бросок на 5 и 10 км. (НФП-2009).mp4",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()

        ex_name = tk.Label(frame_name, text='Упражнение N 48а марш-бросок на 5 км в составе подразделения')
        ex_name.config(font=('Thimes New Roman', 16))
        ex_name.pack(fill='both')
        exer = '''При выполнении упражнений в составе подразделения (взвод, рота и приравненные к ним подразделения) положительная оценка подразделению выставляется при условии, если на финише расстояние между первым и последним военнослужащим составляет не более 50 м. Результат определяется по последнему участнику забега. Граница 50 м перед финишем обозначается яркими флажками с обеих сторон дистанции. Длина коридора измеряется от линии финиша. При выполнении упражнения разрешается взаимопомощь. Запрещается передача оружия и снаряжения.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Потеря (отсутствие) головного убора и снаряжения. 
                '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 30,05
        4 – 30,30
        3 – 31,20
2 курс: 5 – 28,40
        4 – 29,35
        3 – 30,30
3 курс и старше: 
        5 – 28,15
        4 – 29,06
        3 – 30,05
        '''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_6():
        for widget in frame_main.winfo_children():
            widget.destroy()
        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo(
            "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\Упражнение 48,49. Марш-бросок на 5 и 10 км. (НФП-2009).mp4",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()

        ex_name = tk.Label(frame_name, text='Упражнение N 49 марш-бросок на 10 км')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Каждый военнослужащий выполняет упражнение в военной форме одежды с личным оружием (автомат с пристегнутым магазином, сумка для магазинов с одним магазином), противогаз. Запрещается всякое дополнительное крепление оружия и снаряжения, препятствующие их немедленному использованию по назначению (в том числе, дополнительные ремни, другие приспособления, не предусмотренные соответствующей формой одежды). Время определяется каждому участнику забега.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Потеря (отсутствие) головного убора и снаряжения. 
                '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 56,45
        4 – 57,00
        3 – 63,20
2 курс: 5 – 52,12
        4 – 55,30
        3 – 57,00
3 курс и старше: 
        5 – 52,12
        4 – 54,15
        3 – 56,45
        '''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_7():
        for widget in frame_main.winfo_children():
            widget.destroy()
        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo(
            "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\Упражнение 48,49. Марш-бросок на 5 и 10 км. (НФП-2009).mp4",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()

        ex_name = tk.Label(frame_name, text='Упражнение N 49а марш-бросок на 10 км в составе подразделения')
        ex_name.config(font=('Thimes New Roman', 16))
        ex_name.pack(fill='both')
        exer = '''При выполнении упражнений в составе подразделения (взвод, рота и приравненные к ним подразделения) положительная оценка подразделению выставляется при условии, если на финише расстояние между первым и последним военнослужащим составляет не более 50 м. Результат определяется по последнему участнику забега. Граница 50 м перед финишем обозначается яркими флажками с обеих сторон дистанции. Длина коридора измеряется от линии финиша. При выполнении упражнения разрешается взаимопомощь. Запрещается передача оружия и снаряжения.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Потеря (отсутствие) головного убора и снаряжения. 
                '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 66,45
        4 – 67,00
        3 – 73,20
2 курс: 5 – 62,12
        4 – 65,30
        3 – 67,00
3 курс и старше: 
        5 – 62,12
        4 – 64,15
        3 – 66,45
        '''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_8():
        for widget in frame_main.winfo_children():
            widget.destroy()
        for widget in frame_name.winfo_children():
            widget.destroy()

        ex_name = tk.Label(frame_name, text='Упражнение N 53 лыжная гонка на 5 км')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Проводятся на местности вне дорог с общего или раздельного старта по заранее подготовленной трассе. Старт и финиш оборудуются в одном месте.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Финишировать только на 2 лыжах.
2. Запрещается осуществлять снимание лыж и бег с ними.
                '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 25,09
        4 – 25,51
        3 – 27,30
2 курс: 5 – 23,23
        4 – 24,33
        3 – 25,51
3 курс и старше: 
        5 – 22,36
        4 – 24,00
        3 – 25,09
        '''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_9():
        for widget in frame_main.winfo_children():
            widget.destroy()
        for widget in frame_name.winfo_children():
            widget.destroy()

        ex_name = tk.Label(frame_name, text='Упражнение N 54 лыжная гонка на 10 км')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Проводятся на местности вне дорог с общего или раздельного старта по заранее подготовленной трассе. Старт и финиш оборудуются в одном месте.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Финишировать только на 2 лыжах.
2. Запрещается осуществлять снимание лыж и бег с ними.
                '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 63,30
        4 – 66,00
        3 – 71,00
2 курс: 5 – 56,00
        4 – 61,00
        3 – 66,00
3 курс и старше: 
        5 – 53,30
        4 – 58,30
        3 – 63,30
        '''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_10():
        for widget in frame_main.winfo_children():
            widget.destroy()
        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo(
            "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\Упражнение 57. Плавание способом кроль на груди (НФП-2009).mp4",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()

        ex_name = tk.Label(frame_name, text='Упражнение N 57б плавание на 500 м вольным стилем')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Старт выполняется со стартовой тумбой. По команде «ЗАНЯТЬ МЕСТА» – встать на стартовую тумбу, «НА СТАРТ» – ступни ног поставить на ширину 15–20 см, захватить пальцами передний край тумбы, ноги согнуть в коленях, туловище наклонить вперед, руки отвести назад, «МАРШ» – сделать взмах руками и оттолкнуться ногами от тумбы вперед-вверх, в полете выпрямить тело, руки вытянуть вперед. При плавании вольным стилем применяется любой способ. Поворот выполнять с обязательным касанием стенки любой частью тела.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Во время поворота запрещается ставить ноги на дно бассейна.
                '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 12,45
        4 – 13,10
        3 – 14,00
2 курс: 5 – 11,30
        4 – 12,20
        3 – 13,10
3 курс и старше: 
        5 – 11,05
        4 – 11,55
        3 – 12,45
        '''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)




    botton_sila_1 = ttk.Button(frame_ex, text='Упражнение №45 бег на 1 км', command=sila_1).pack(fill='both')
    botton_sila_2 = ttk.Button(frame_ex, text='Упражнение №46 бег на 3 км', command=sila_2).pack(fill='both')
    botton_sila_3 = ttk.Button(frame_ex, text='Упражнение №47 бег на 5 км', command=sila_3).pack(fill='both')
    botton_sila_4 = ttk.Button(frame_ex, text='Упражнение №48 марш бросок на 5 км', command=sila_4).pack(fill='both')
    botton_sila_5 = ttk.Button(frame_ex, text='Упражнение №48а марш бросок на 5 км в составе подразделения', command=sila_5).pack(fill='both')
    botton_sila_6 = ttk.Button(frame_ex, text='Упражнение №49 марш бросок на 10 км', command=sila_6).pack(fill='both')
    botton_sila_7 = ttk.Button(frame_ex, text='Упражнение №49а марш бросок на 10 км в составе подразделения', command=sila_7).pack(fill='both')
    botton_sila_8 = ttk.Button(frame_ex, text='Упражнение №53 лыжная гонка на 5 км', command=sila_8).pack(fill='both')
    botton_sila_9 = ttk.Button(frame_ex, text='Упражнение №54 лыжная гонка на 10 км', command=sila_9).pack(fill='both')
    botton_sila_10 = ttk.Button(frame_ex, text='Упражнение №57б плавание на 500 м вольным стилем', command=sila_10).pack(fill='both')


def bystrota():
    for widget in frame_ex.winfo_children():
        widget.destroy()

    def sila_1():
        for widget in frame_main.winfo_children():
            widget.destroy()

        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo(
            "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\Упражнение 40_41. Бег на 60_100м (НФП-2009).mp4",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()
        ex_name = tk.Label(frame_name, text='Упражнение N 40 бег на 60 м')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Выполняются с высокого старта по беговой дорожке стадиона или ровной площадке с любым покрытием'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Осуществлять бег только по своей дорожки. 
2. Пересечение линии своей дорожки считается невыполнением упражнения. 
3. Допускается 1 фальш-старт в забеге.
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 8,3
        4 – 8,4
        3 – 8,6
2 курс: 5 – 8,0
        4 – 8,2
        3 – 8,4
3 курс и старше: 
        5 – 7,9
        4 – 8,1
        3 – 8,3
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_2():
        for widget in frame_main.winfo_children():
            widget.destroy()

        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo(
            "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\Упражнение 40_41. Бег на 60_100м (НФП-2009).mp4",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()
        ex_name = tk.Label(frame_name, text='Упражнение N 41 бег на 100 м')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Выполняются с высокого старта по беговой дорожке стадиона или ровной площадке с любым покрытием'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Осуществлять бег только по своей дорожки. 
2. Пересечение линии своей дорожки считается невыполнением упражнения. 
3. Допускается 1 фальш-старт в забеге.
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 13,7
        4 – 13,9
        3 – 14,4
2 курс: 5 – 13,2
        4 – 13,6
        3 – 13,9
3 курс и старше: 
        5 – 13,0
        4 – 13,4
        3 – 13,7
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_3():
        for widget in frame_main.winfo_children():
            widget.destroy()

        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo(
            "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\Упражнение 42. Челночный бег 10х10 м. (НФП-2009).mp4",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()
        ex_name = tk.Label(frame_name, text='Упражнение N 42 Челночный бег 10 х 10 м')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Выполняется на ровной площадке с размеченными линиями старта и поворота. Ширина линии старта и поворота входит в отрезок 10 м. По команде «МАРШ» пробежать 10 м, коснуться земли за линией поворота любой частью тела, повернуться кругом, пробежать таким образом еще девять отрезков по 10 м. Запрещается использовать в качестве опоры при повороте какие-либо естественные или искусственные предметы, неровности, выступающие над поверхностью дорожки.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Не пересечение линии поворота.
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 26,8
        4 – 27,0
        3 – 27,3
2 курс: 5 – 26,3
        4 – 26,7
        3 – 27,0
3 курс и старше: 
        5 – 26,2
        4 – 26,5
        3 – 26,8
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_4():
        for widget in frame_main.winfo_children():
            widget.destroy()

        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo(
            "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\Упражнение 43_45_46_47 бег на 400м_1км_3км_5км (НФП-2009).mp4",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()
        ex_name = tk.Label(frame_name, text='Упражнение N 43 бег на 400 м')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Выполняются с высокого старта по беговой дорожке стадиона или ровной площадке с любым покрытием'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Осуществлять бег только по своей дорожки. 
2. Пересечение линии своей дорожки считается невыполнением упражнения. 
3. Допускается 1 фальш-старт в забеге.
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 1,05,3
        4 – 1,06,5
        3 – 1,10
2 курс: 5 – 1,02,4
        4 – 1,04,2
        3 – 1,06,5
3 курс и старше: 
        5 – 1,01,7
        4 – 1,03,2
        3 – 1,05.3
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_5():
        for widget in frame_main.winfo_children():
            widget.destroy()

        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo(
            "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\Упражнение 44. Челночный бег 4х100 метров (НФП-2009).mp4",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()
        ex_name = tk.Label(frame_name, text='Упражнение N 44. Челночный бег 4 х 100 м')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Выполняется на беговой дорожке стадиона с высокого старта по прямым дорожкам стадиона (100 м) или другой ровной площадке, с размеченными дорожками (ширина – 1,25 м), линией старта и линией поворота. Для каждого стартующего посередине дорожки на расстоянии 2,5 м от линии старта и поворота устанавливаются два флажка яркого цвета высотой 0,5-0,75 м. Каждый участник стартует справа от своего флажка. Оббегание флажков происходит против часовой стрелки. Всего преодолеваются 4 отрезка.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Осуществлять бег только по своей дорожки. 
2. Пересечение линии своей дорожки считается невыполнением упражнения. 
3. Допускается 1 фальш-старт в забеге.
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 1,09,3
        4 – 1,10,5
        3 – 1,14
2 курс: 5 – 1,06,4
        4 – 1,08,2
        3 – 1,10,5
3 курс и старше: 
        5 – 1,05,7
        4 – 1,07,2
        3 – 1,09,3
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_6():
        for widget in frame_main.winfo_children():
            widget.destroy()

        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo(
            "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\Упражнение 57. Плавание способом кроль на груди (НФП-2009).mp4",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()
        ex_name = tk.Label(frame_name, text='Упражнение N 57 Плавание на 100 м вольным стилем')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Старт выполняется со стартовой тумбой. По команде «ЗАНЯТЬ МЕСТА» – встать на стартовую тумбу, «НА СТАРТ» – ступни ног поставить на ширину 15–20 см, захватить пальцами передний край тумбы, ноги согнуть в коленях, туловище наклонить вперед, руки отвести назад, «МАРШ» – сделать взмах руками и оттолкнуться ногами от тумбы вперед-вверх, в полете выпрямить тело, руки вытянуть вперед. При плавании вольным стилем применяется любой способ. Поворот выполнять с обязательным касанием стенки любой частью тела.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Во время поворота запрещается ставить ноги на дно бассейна.
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 1,45
        4 – 1,50
        3 – 2,00
2 курс: 5 – 1,30
        4 – 1,40
        3 – 1,50
3 курс и старше: 
        5 – 1,25
        4 – 1,35
        3 – 1,45
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_7():
        for widget in frame_main.winfo_children():
            widget.destroy()

        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo(
            "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\Упражнение 57. Плавание способом кроль на груди (НФП-2009).mp4",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()
        ex_name = tk.Label(frame_name, text='Упражнение N 57а плавание на 50 м вольным стилем')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Выполняются с высокого старта по беговой дорожке стадиона или ровной площадке с любым покрытием'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Во время поворота запрещается ставить ноги на дно бассейна.
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 43,5
        4 – 45,0
        3 – 48,0
2 курс: 5 – 39,0
        4 – 42,0
        3 – 45,0
3 курс и старше: 
        5 – 37,5
        4 – 40,5
        3 – 43,5
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_8():
        for widget in frame_main.winfo_children():
            widget.destroy()

        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo(
            "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\Упражнение 57. Плавание способом кроль на груди (НФП-2009).mp4",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()
        ex_name = tk.Label(frame_name, text='Упражнение N 57б плавание на 500 м вольным стилем')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Старт выполняется со стартовой тумбой. По команде «ЗАНЯТЬ МЕСТА» – встать на стартовую тумбу, «НА СТАРТ» – ступни ног поставить на ширину 15–20 см, захватить пальцами передний край тумбы, ноги согнуть в коленях, туловище наклонить вперед, руки отвести назад, «МАРШ» – сделать взмах руками и оттолкнуться ногами от тумбы вперед-вверх, в полете выпрямить тело, руки вытянуть вперед. При плавании вольным стилем применяется любой способ. Поворот выполнять с обязательным касанием стенки любой частью тела.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Во время поворота запрещается ставить ноги на дно бассейна.
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 12,45
        4 – 13,10
        3 – 14,00
2 курс: 5 – 11,30
        4 – 12,20
        3 – 13,10
3 курс и старше: 
        5 – 11,05
        4 – 11,55
        3 – 12,45
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)



    botton_sila_1 = ttk.Button(frame_ex, text='Упражнение №40 бег на 60 м', command=sila_1).pack(fill='both')
    botton_sila_2 = ttk.Button(frame_ex, text='Упражнение №41 бег на 100 м', command=sila_2).pack(fill='both')
    botton_sila_4 = ttk.Button(frame_ex, text='Упражнение №42 Челночный бег 10 х 10 м', command=sila_3).pack(fill='both')
    botton_sila_5 = ttk.Button(frame_ex, text='Упражнение №43 бег на 400 м', command=sila_4).pack(fill='both')
    botton_sila_6 = ttk.Button(frame_ex, text='Упражнение №44 челночный бег 4 х 100 м', command=sila_5).pack(fill='both')
    botton_sila_7 = ttk.Button(frame_ex, text='Упражнение №57 плавание на 100 м', command=sila_6).pack(fill='both')
    botton_sila_9 = ttk.Button(frame_ex, text='Упражнение №57а плавание на 50 м вольным стилем', command=sila_7).pack(fill='both')



def lovkost():
    for widget in frame_ex.winfo_children():
        widget.destroy()

    def sila_1():
        for widget in frame_main.winfo_children():
            widget.destroy()

        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo(
            "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\file_20.mp4",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()
        ex_name = tk.Label(frame_name, text='Упражнение 20. Соскок махом назад на перекладине для 1-2 курсов')
        ex_name.config(font=('Thimes New Roman', 16))
        ex_name.pack(fill='both')
        exer = '''Для курсантов 1-го курса военно-учебных заведений: подъем переворотом, мах дугой, соскок махом назад. Для курсантов 2-го курса военно-учебных заведений: вис, размахивание, подъем завесом правой (левой) вне, пере мах ноги назад в упор, мах дугой, соскок махом назад. Разрешается, незначительное сгибание и разведение ног, неустойчивое приземление'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Сгибание и разведение ног.
2. Сгибание туловища при обороте назад.
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 55
        4 – 50
        3 – 40
2 курс: 5 – 70
        4 – 60
        3 – 50
3 курс и старше: 
        5 – 75
        4 – 65
        3 – 55
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_2():
        for widget in frame_main.winfo_children():
            widget.destroy()

        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo(
            "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\file_21.mp4",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()
        ex_name = tk.Label(frame_name, text='Упражнение 21. Соскок махом вперед на брусьях ')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Для курсантов 1-го курса военно-учебных заведений: упор на руках, размахивание, подъем махом вперед в сед ноги врозь, пере мах ног внутрь и мах назад, махом вперед соскок вправо с поворотом налево, держась за жердь двумя руками. Для курсантов 2-го курса военно-учебных заведений: упор на руках, размахивание, подъем махом вперед в сед ноги врозь, перехват рук вперед, кувырок вперед в сед ноги врозь, пере мах ног внутрь и мах назад, махом вперед соскок вправо с поворотом налево, держась за жердь двумя руками. Для курсантов 3-го и старших курсов военно-учебных заведений: упор на руках, размахивание, подъем махом вперед, мах назад, мах вперед в сед ноги врозь, перехват рук вперед, силой стойка на плечах (держать 2 с), кувырок вперед в сед ноги врозь, пере мах ног внутрь и мах назад, махом вперед соскок вправо с поворотом налево, держась за жердь двумя руками. Разрешается выполнять соскок махом вперед в другую сторону'''
        t = tk.Text(frame_main, height=18, width=65)
        t.config(font=('Thimes New Roman', 8))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Сгибание и разведение ног. 
2. Малая амплитуда выполнения упражнения.
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 55
        4 – 50
        3 – 40
2 курс: 5 – 70
        4 – 60
        3 – 50
3 курс и старше: 
        5 – 75
        4 – 65
        3 – 55
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_3():
        for widget in frame_main.winfo_children():
            widget.destroy()

        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo(
            "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\file_51.mp4",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()
        ex_name = tk.Label(frame_name, text='Упражнение N 51 тройной прыжок с места')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Выполняется на ровной площадке с любым покрытием, с размеченной линией отталкивания и местом приземления, и контрольными отметками через каждые 5 см. Результат определяется по ближайшей к линии отталкивания отметке (следу), оставленной любой частью тела с точностью до 1 см. Предоставляется три попытки. Зачет по лучшему результату.'''

        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Заступ за линию.
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 625
        4 – 610
        3 – 580
2 курс: 5 – 700
        4 – 640
        3 – 610
3 курс и старше: 
        5 – 724
        4 – 670
        3 – 625
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_4():
        for widget in frame_main.winfo_children():
            widget.destroy()

        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo(
            "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\file_52.mp4",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()
        ex_name = tk.Label(frame_name, text='Упражнение N 52 метание гранаты 600 г на дальность')
        ex_name.config(font=('Thimes New Roman', 20))
        ex_name.pack(fill='both')
        exer = '''Для метания используют болванки учебных гранат. Вес гранаты - 600 граммов. Метание гранаты на дальность осуществляется в сектор шириной 10 метров (включая ширину линии разметки). Коридор для разбега – 3 м. Предоставляется три попытки. Зачет по лучшему результату.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Заступ за линию. 
2. Выход гранаты за коридор.
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 34
        4 – 32
        3 – 30
2 курс: 5 – 40
        4 – 35
        3 – 32
3 курс и старше: 
        5 – 42
        4 – 37
        3 – 34
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    botton_sila_1 = ttk.Button(frame_ex, text='Упражнение №20 Соскок махом назад на перекладине для 1-2 курсов', command=sila_1).pack(fill='both')
    botton_sila_2 = ttk.Button(frame_ex, text='Упражнение №21 Соскок махом вперед на брусьях', command=sila_2).pack(fill='both')
    botton_sila_4 = ttk.Button(frame_ex, text='Упражнение №51 Тройной прыжок с места', command=sila_3).pack(fill='both')
    botton_sila_5 = ttk.Button(frame_ex, text='Упражнение №52 Метание гранаты 600г на дальность', command=sila_4).pack(fill='both')


def VP():
    for widget in frame_ex.winfo_children():
        widget.destroy()

    def sila_1():
        for widget in frame_main.winfo_children():
            widget.destroy()

        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo(
            "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\file_30.mp4",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()
        ex_name = tk.Label(frame_name, text='Упражнение 30. Комплекс приёмов рукопашного боя без оружия на 8 счетов')
        ex_name.config(font=('Thimes New Roman', 15))
        ex_name.pack(fill='both')
        exer = '''Исходное положение - строевая стойка «Раз» - С шагом левой ногой вперед изготовиться к бою. «Два» - Выполнить левой рукой отбив вверх и удар правой рукой вперед прямо. «Три» - Выполнить удар правой ногой вперед прямо или снизу. «Четыре» - С разворотом на 90º и с шагом правой ноги выполнить удар в сторону слева наотмашь ребром ладони правой руки. «Пять» - С шагом правой ногой назад выполнить левой рукой отбив внутрь. «Шесть» - С шагом правой ногой вперед выполнить удар кулаком правой руки вперед сверху. «Семь» - Выполнить удар левой ногой вперед прямо и принять левостороннюю изготовку к бою. «Восемь» - С шагом левой ногой и поворотом налево принять строевую стойку.'''
        t = tk.Text(frame_main, height=15, width=65)
        t.config(font=('Thimes New Roman', 11))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Отсутствие фиксации каждого элемента. 
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 55
        4 – 50
        3 – 40
2 курс: 5 – 70
        4 – 60
        3 – 50
3 курс и старше: 
        5 – 75
        4 – 65
        3 – 55
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_2():
        for widget in frame_main.winfo_children():
            widget.destroy()

        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo(
            "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\file_31.mp4",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()
        ex_name = tk.Label(frame_name, text='Упражнение 31. Комплекс рукопашного боя с автоматом на 8 счетов')
        ex_name.config(font=('Thimes New Roman', 15))
        ex_name.pack(fill='both')
        exer = '''Упражнение 31. Комплекс рукопашного боя с автоматом на 8 счетов  Исходное положение - строевая стойка.
«Раз» - С шагом левой ногой вперед изготовиться к бою. «Два» - Выполнить стволом автомата отбив вправо и укол штыком (тычок стволом) с выпадом левой ногой. «Три» - С шагом правой ногой назад выполнить удар затыльником приклада назад прямо. «Четыре» - Поворачиваясь на левой ноге направо, с шагом правой назад выполнить стволом автомата отбив влево. «Пять» - С коротким шагом правой ногой вперед выполнить удар прикладом сбоку. «Шесть» - С поворотом кругом через левое плечо, отставляя правую ногу назад, защититься подставкой автомата от удара снизу. «Семь» - С шагом правой ногой вперед выполнить удар магазином вперед прямо и - рубящий удар штыком (стволом) слева – направо вниз. «Восемь» - С шагом правой ногой назад и поворотом направо принять строевую стойку.
'''
        t = tk.Text(frame_main, height=18, width=65)
        t.config(font=('Thimes New Roman', 8))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Отсутствие фиксации каждого элемента. 
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 55
        4 – 50
        3 – 40
2 курс: 5 – 70
        4 – 60
        3 – 50
3 курс и старше: 
        5 – 75
        4 – 65
        3 – 55
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    def sila_3():
        for widget in frame_main.winfo_children():
            widget.destroy()

        for widget in frame_name.winfo_children():
            widget.destroy()
        video = tkvideo(
            "C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\фп\\видео\\file_32.mp4",
            frame_video, loop=1,
            size=(1068, 534))
        video.play()
        ex_name = tk.Label(frame_name, text='Упражнение N 32 общее контрольное упражнение на единой полосе препятствий')
        ex_name.config(font=('Thimes New Roman', 15))
        ex_name.pack(fill='both')
        exer = '''Выполняется в военной форме одежды без оружия. Дистанция – 400 м. Исходное положение - стоя в траншее; метнуть 3 гранаты массой 600 г из траншеи на 20 м по стенке (проломам) или по площадке 1 x 2,6 м перед стенкой (засчитывается прямое попадание); при непопадании в цель первой гранатой продолжать метание, но не более трех гранат до поражения цели (в случае непопадания гранатой в цель от количества баллов, полученных за упражнение, отнимается десять баллов); выскочить из траншеи, пробежать 100 м по дорожке по направлению к линии начала полосы; обежать флажок и перепрыгнуть ров шириной 2,5 м; пробежать по проходам лабиринта; перелезть через забор, влезть по вертикальной лестнице на второй (изогнутый) отрезок разрушенного моста; пробежать по балкам, перепрыгнув через разрыв, и соскочить на землю из положения стоя с конца последнего отрезка балки; преодолеть три ступени разрушенной лестницы с обязательным касанием двумя ногами земли между ступенями, пробежать под четвертой ступенью; пролезть в пролом стенки; соскочить в траншею, пройти по ходу сообщения; выскочить из колодца; прыжком преодолеть стенку; взбежать по наклонной лестнице на четвертую ступень и сбежать по ступеням разрушенной лестницы; влезть по вертикальной лестнице на балку разрушенного моста, пробежать по балкам, перепрыгивая через разрывы, и сбежать по наклонной доске; перепрыгнуть ров шириной 2 м; пробежать 20 м и, обежав флажок, пробежать в обратном направлении 100 м по дорожке.'''
        t = tk.Text(frame_main, height=18, width=100)
        t.config(font=('Thimes New Roman', 8))
        t.grid()
        t.insert(tk.END, exer)
        mark = '''
1. Непопадание гранаты в каменную стенку. 
        '''
        tmark = tk.Text(frame_main, height=15, width=20)
        tmark.config(font=('Thimes New Roman', 11))
        tmark.grid(row=0, column=1)
        tmark.insert(tk.END, mark)
        markc = '''
1 курс: 5 – 8,3
        4 – 8,4
        3 – 8,6
2 курс: 5 – 8,0
        4 – 8,2
        3 – 8,4
3 курс и старше: 
        5 – 7,9
        4 – 8,1
        3 – 8,3
'''
        tmarkc = tk.Text(frame_main, height=15, width=40)
        tmarkc.config(font=('Thimes New Roman', 11))
        tmarkc.grid(row=0, column=2)
        tmarkc.insert(tk.END, markc)

    botton_sila_1 = ttk.Button(frame_ex, text='Упражнение №30 Комплекс приемов рукопашного боя без оружия на 8 счетов', command=sila_1).pack(fill='both')
    botton_sila_2 = ttk.Button(frame_ex, text='Упражнение №31 Комплекс рукопашного боя с автоматом на 8 счетов', command=sila_2).pack(fill='both')
    botton_sila_4 = ttk.Button(frame_ex, text='Упражнение №32 Общее контрольное упражнение на единой полосе препятствий', command=sila_3).pack(fill='both')



botton_sila = ttk.Button(frame_home, text='Сила', command=sila).pack()
botton_vinoslivost = ttk.Button(frame_home, text='Выносливость', command=vinoslivost).pack()
botton_bystrota = ttk.Button(frame_home, text='Быстрота', command=bystrota).pack()
botton_lovkost = ttk.Button(frame_home, text='Ловкость', command=lovkost).pack()
botton_VP = ttk.Button(frame_home, text='Военно-прикладные навыки', command=VP).pack()

window.mainloop()

