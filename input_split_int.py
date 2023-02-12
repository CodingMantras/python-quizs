# Enter your code here. Read input from STDIN. Print output to STDOUT
# n = int(input())
# eng = set(map(int, input().split()))
# b = int(input())
# fr = set(map(int, input().split()))
# print(len(eng.intersection(fr)))

# def set_op(first_set, op_name, other_set):
#     if op_name == "intersection_update":
#         first_set.intersection_update(other_set)
#     if op_name == "difference_update":
#         first_set.difference_update(other_set)
#     if op_name == "symmetric_difference_update":
#         first_set.symmetric_difference_update(other_set)
#     if op_name == "update":
#         first_set.update(other_set)
#     return first_set


# n = int(input())
# first_set = set(map(int, input().split()))
# N = int(input())
# result = []

# for i in range(N):
#     op_name, length = input().split()
#     other_set = set(map(int, input().split()))
#     res = set_op(first_set, op_name, other_set)
#     result.append(res)
# print(result)
# print(len(set(result)))

from collections import Counter


def find_captain(room_numbers, k):
    # Use Counter to count the occurrences of each room number
    room_counts = Counter(room_numbers)
    print(f"{room_counts=}")
    # Iterate through the Counter object
    for room, count in room_counts.items():
        # If the count is 1, return the room number as it's the captain's room
        if count == 1:
            return room
    # If no room with count 1 is found, return None
    return None


# Example usage
room_numbers = [1, 2, 3, 4, 5, 10, 10, 10, 10, 15, 15, 20, 20, 20]
k = 3
captain_room = find_captain(room_numbers, k)
print(captain_room)  # Output: 1
