vote_num = 0


def vote():
    print("touhyou")
    global vote_num
    vote_num += 1


def reset_box():
    global vote_num
    print("hakowokara")
    vote_num = 0


def check_box():
    global vote_num
    print("hyou{}desu".format(vote_num))
