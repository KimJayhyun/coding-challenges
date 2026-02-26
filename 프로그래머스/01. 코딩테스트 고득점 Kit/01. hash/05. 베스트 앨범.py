# https://school.programmers.co.kr/learn/courses/30/lessons/42579

import heapq


def solution(genres: list, plays: list):
    genre_play_dict = {}
    genre_total_play_dict = {}
    for index in range(len(genres)):
        genre = genres[index]
        play_count = plays[index]

        if genre not in genre_play_dict:
            genre_play_dict[genre] = []
            genre_total_play_dict[genre] = 0

        heapq.heappush(genre_play_dict[genre], (-play_count, index))
        genre_total_play_dict[genre] += play_count

    total_count_genre_dict = {}
    for genre, play in genre_total_play_dict.items():
        total_count_genre_dict[play] = genre

    ordered_play_list: list = list(total_count_genre_dict.keys())
    ordered_play_list.sort(reverse=True)

    result = []
    for play in ordered_play_list:
        ordered_genre = total_count_genre_dict[play]

        heap = genre_play_dict[ordered_genre]
        largest: list = heapq.nsmallest(2, heap)

        for _, index in largest:
            result.append(index)

    return result


print(
    solution(
        ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
    )
)
"    == [4, 1, 3, 0]"
