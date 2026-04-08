# Время выполнения: O(n*log(n))
# Память: O(n)

def count_meeting_rooms(segments: list[list[int]]) -> int:
    points = []
    for seg in segments:
        points.extend([[seg[0], +1], [seg[1], -1]])

    points.sort()

    max_room = 0
    curr_rooms = 0

    for point in points:
        curr_rooms += point[1]
        max_room = max(max_room, curr_rooms)

    return max_room
        
print(count_meeting_rooms([[2,5], [1,3], [2,4]]))