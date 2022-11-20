import PySimpleGUI as sg
from find_IMDb_rating import find_movie

event, values = sg.Window('Browse Folder', [[sg.Text('Folder Path')], [sg.Input(), sg.FolderBrowse()], [sg.OK(), sg.Cancel()] ]).read(close=True)
names,rating,genres = find_movie(values[0])

header =  [[sg.Text('Movie',size=(100,1)),sg.Text('Rating',size=(10,1)),sg.Text('Genres',size=(25,1))]]
input_rows = [[sg.Text(names[i],size=(55,1)),sg.Text(rating[i],size=(3,2)),sg.Text(genres[i],size=(25,1))] for i in range(len(names))]

layout = header + input_rows
window = sg.Window('Movie Rating and Genres', layout, font='Italian 12')
event, values = window.read(close=True)
