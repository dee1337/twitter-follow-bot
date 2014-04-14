from klout import *

# ----------- START: CONFIG! ---------------#
APIKEY = 'PUT YOUR API KEY INSIDE!!'
# put as much as you want - without @ prefix:
users = ['placeholder-user1', 'placeholder-user2', 'placeholder-user3']
# ------------- END: CONFIG! ---------------#


k = Klout(APIKEY)
def getKloutId(name):
    return k.identity.klout(screenName=name).get('id')


def getKloutScore(name):
    kid = getKloutId(name)
    return round(k.user.score(kloutId=kid).get('score'), 2)


def getChanges(name):
    """ returns a list with 3 rounded values:
    [dayChange, monthChange, weekChange]
    """
    kid = getKloutId(name)
    changes = k.user.score(kloutId=kid).get('scoreDelta')
    return [round(changes["dayChange"], 2), round(changes["weekChange"], 2), round(changes["monthChange"], 2)]


# print getKloutScore(users[0])
def checkScores(userlist):
    "*" * 50, "CHECKING KLOUT SCORE DEVELOPMENTS", "*" * 50
    collection = []
    for user in userlist:
        score = getKloutScore(user)
        changes = getChanges(user)
        print "User %s has a score of %d" % (user.upper(), round(score,2))
        print "changes: in 24h by {0} | this week by {1} | this month by {2}".format(round(changes[0], 2), round(changes[1],2), round(changes[2],2))
        print "-"*100
        collection.append((user, score, changes))
    return collection
