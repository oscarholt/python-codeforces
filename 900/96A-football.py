def main():
    player_positions = list(input())
    dangerous_count = 0

    for i in range(len(player_positions)):
        player = player_positions[i]

        # Determine if there can be another 6 of the same player
        if i + 6 <= len(player_positions) - 1:
            dangerous = 1
            for j in range(1, 7):
                if player_positions[i + j] != player:
                    dangerous = 0
            if dangerous:
                dangerous_count += 1

    if(dangerous_count > 0):
        print('YES')
    else:
        print('NO')

main()
