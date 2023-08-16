import matplotlib.pyplot as plt

def coffee_sleep(n=5):
    coffee = []
    sleep = []
    for i in range(n):
        coffee.append(int(input("Enter amount of coffee you drink per week:")))
        sleep.append(int(input("Enter average sleep duration per night:")))
    return coffee, sleep

def movies(n=5):
    movie = {}
    for i in range(n):
        genre = input("Enter your favourite movie genre:")
        movie[genre] = movie.get(genre, 0) + 1
    return movie

def song(n=5):
    song = {}
    for i in range(n):
        genre = input("Enter your favourite music genre:")
        song[genre] = song.get(genre, 0) + 1
    return song

def mm_vs_dd(n=5):
    mm, dd = 0,0
    for i in range(n):
        ans = input("Who wins? Micky mouse or Donald Duck?")
        if ans.lower() == "":






