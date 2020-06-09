t = "a", "b", "c"
print(t)

print("a", "b", "c")
print(("a", "b", "c"))

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "bad company", "bad company", 1974
budgie = "Nightflight", "Budgie", 1981
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

# metallica2 = ("Ride the Lightning", "Metallica", 1984)
# print(metallica2)
# metallica2[0] = "Master of Puppets"
# print(metallica2)

# imelda = "More Mayhem", "Emilda May", 2011
# imelda = imelda[0], "Imelda May", imelda[2]
# print(imelda)

imelda = "More Mayhem", "Imelda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])
print(imelda)

imelda[3].append((5, "All for You"))

title, artist, year, tracks = imelda
tracks.append((6, "Eternity"))
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTrack number {}, title: {}".format(track, title))