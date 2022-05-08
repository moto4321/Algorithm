# https://programmers.co.kr/learn/courses/30/lessons/17683

def change(arr):
    if 'A#' in arr:
        arr = arr.replace('A#', 'a')
    if 'C#' in arr:
        arr = arr.replace('C#', 'c')
    if 'D#' in arr:
        arr = arr.replace('D#', 'd')
    if 'F#' in arr:
        arr = arr.replace('F#', 'f')
    if 'G#' in arr:
        arr = arr.replace('G#', 'g')
    return arr


def solution(m, musicinfos):  # m = ABC
    answer = []

    for i in range(len(musicinfos)):
        music = musicinfos[i].split(',')
        start_time = music[0].split(':')
        end_time = music[1].split(':')
        title = music[2]  # HELLO
        acbo = music[3]  # C#DEFGAB
        acbo = change(acbo)

        longing_time = (int(end_time[0]) * 60 + int(end_time[1])) - (int(start_time[0]) * 60 + int(start_time[1]))

        longing_acbo = acbo * (longing_time // len(acbo)) + acbo[:longing_time % len(acbo)]

        if change(m) in longing_acbo:
            answer.append((title, longing_time, start_time))

    if len(answer) > 1:
        answer = sorted(answer, key=lambda x: (-x[1], x[2]))
        return answer[0][0]
    elif len(answer) == 1:
        return answer[0][0]
    elif len(answer) == 0:
        return "(None)"