def reward_action(player, action):
    points_table = {
        "message": 1,
        "invite": 10,
        "challenge": 5,
        "like": 0.5
    }
    points = points_table.get(action, 0)
    player.add_points(points)
