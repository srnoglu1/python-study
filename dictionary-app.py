players = {}

id = input('Player number: ')
name = input('Player name: ')
yearOfBirth = input('Birth year: ')
nationalty = input('Country: ')
history = input('Team History played: ')

players.update({
    id: {
    "name":name,
    "yearOfBirth":yearOfBirth,
    "nationalty":nationalty,
    "history":history.split(',')
    }
})
print(players)
